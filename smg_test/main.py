#!/usr/local/bin/python3
import minimalmodbus
import serial

# https://github.com/syssi/esphome-smg-ii
# https://minimalmodbus.readthedocs.io/en/stable/readme.html

# Host computer: 01 03 00 CA 00 03 25 F5
# Lower computer: 01 03 06 08 FC 13 88 04 B0 F7 F3
def test_read_example():
    registers = instr.read_registers(202, 3, 3)
    print(registers)

test_cmds = {
    'battery_voltage': {
        'cmd': (215, 1, 3, True),
        'name': 'Battery average voltage',
        'unit_of_measurement': 'V',
    },
    'battery_current': {
        'cmd': (216, 1, 3, True),
        'name': 'Battery average current',
        'unit_of_measurement': 'A',
    },
    'battery_power': {
        'cmd': (217, 0, 3, True),
        'name': 'Battery average power',
        'unit_of_measurement': 'W',
    },
    'pv_voltage': {
        'cmd': (219, 1, 3, True),
        'name': 'PV average voltage',
        'unit_of_measurement': 'V',
    },
    'pv_current': {
        'cmd': (220, 1, 3, True),
        'name': 'PV average Current',
        'unit_of_measurement': 'A',
    },
    'pv_power': {
        'cmd': (223, 0, 3, True),
        'name': 'PV average power',
        'unit_of_measurement': 'W',
    },
    'pv_charge_power': {
        'cmd': (224, 0, 3, True),
        'name': 'PV charging average power',
        'unit_of_measurement': 'A',
    },
    'mains_voltage': {
        'cmd': (202, 1, 3, True),
        'name': 'Effective mains voltage',
        'unit_of_measurement': 'V',
    },
    'mains_frequency': {
        'cmd': (203, 2, 3, True),
        'name': 'Mains Frequency',
        'unit_of_measurement': 'Hz',
    },
    'mains_power': {
        'cmd': (204, 0, 3, True),
        'name': 'Average mains power',
        'unit_of_measurement': 'W',
    },
    'inverter_voltage': {
        'cmd': (205, 1, 3, True),
        'name': 'Effective inverter voltage',
        'unit_of_measurement': 'V',
    },
    'inverter_current': {
        'cmd': (206, 1, 3, True),
        'name': 'Effective inverter current',
        'unit_of_measurement': 'A',
    },
    'inverter_frequency': {
        'cmd': (207, 2, 3, False),
        'name': 'Inverter frequency',
        'unit_of_measurement': 'Hz',
    },
    'inverter_power': {
        'cmd': (208, 0, 3, True),
        'name': 'Average inverter power',
        'unit_of_measurement': 'W',
    },
    'inverter_charging_power': {
        'cmd': (209, 0, 3, True),
        'name': 'Inverter charging power',
        'unit_of_measurement': 'W',
    },
    'output_voltage': {
        'cmd': (210, 1, 3, True),
        'name': 'Output effective voltage',
        'unit_of_measurement': 'V',
    },
    'output_current': {
        'cmd': (211, 1, 3, True),
        'name': 'Output effective Current',
        'unit_of_measurement': 'A',
    },
    'output_frequency': {
        'cmd': (207, 2, 3, False),
        'name': 'Output frequency',
        'unit_of_measurement': 'Hz',
    },
    'output_power': {
        'cmd': (213, 0, 3, True),
        'name': 'Output active power',
        'unit_of_measurement': 'W',
    },
    'output_apparent_power': {
        'cmd': (214, 0, 3, True),
        'name': 'Output apparent power',
        'unit_of_measurement': 'VA',
    },
    'temp_dcdc': {
        'cmd': (226, 0, 3, True),
        'name': 'DCDC Temperature',
        'unit_of_measurement': 'C',
    },
    'temp_inverter': {
        'cmd': (227, 0, 3, True),
        'name': 'Inverter Temperature',
        'unit_of_measurement': 'C',
    },
    'battery_soc': {
        'cmd': (229, 0, 3, True),
        'name': 'Battery State of Charge',
        'unit_of_measurement': '%',
    },
    'load_percentage': {
        'cmd': (225, 0, 3, True),
        'name': 'Load percentage',
        'unit_of_measurement': '%',
    },
    'working_mode': {
        'cmd': (201, 0, 3, False),
        'name': 'Working Mode',
        'unit_of_measurement': '-',
    },
}


def test_read_example_with_values():
    instr.debug = False
    for name, vals in test_cmds.items():
         try:
             registers = instr.read_register(*vals['cmd'])
             print("{} - '{}':{} [{}]".format(name,vals['name'],registers,vals['unit_of_measurement']))
         except IOError:
             print("Failed to read from device - {}".format(name))
         except Exception as error:
             print(f"Exception {error=}, {type(error)=}")
             exit(1)

if __name__ == "__main__":
    try:
        instr = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
        instr.serial.baudrate = 9600
        instr.serial.parity=serial.PARITY_NONE
        instr.serial.timeout = 1
        instr.debug = True
    except IOError:
        print("Failed to open device")
        exit(1)
    except Exception as err:
        print(f"Failed to open device {err=}, {type(err)=}")
        exit(1)

    # test_read_example()
    test_read_example_with_values()