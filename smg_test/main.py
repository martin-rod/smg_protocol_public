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
        'cmd_read_register': (215, 1, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Battery average voltage',
        'unit': 'V',
    },
    'battery_current': {
        'cmd_read_register': (216, 1, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Battery average current',
        'unit': 'A',
    },
    'battery_current_2': {
        'cmd_read_register': (232, 1, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Battery average current 2',
        'unit': 'A',
    },
    'battery_power': {
        'cmd_read_register': (217, 0, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Battery average power',
        'unit': 'W',
    },
    'pv_voltage': {
        'cmd_read_register': (219, 1, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'PV average voltage',
        'unit': 'V',
    },
    'pv_current': {
        'cmd_read_register': (220, 1, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'PV average Current',
        'unit': 'A',
    },
    'pv_power': {
        'cmd_read_register': (223, 0, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'PV average power',
        'unit': 'W',
    },
    'pv_charge_power': {
        'cmd_read_register': (224, 0, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'PV charging average power',
        'unit': 'A',
    },
    'mains_voltage': {
        'cmd_read_register': (202, 1, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Effective mains voltage',
        'unit': 'V',
    },
    'mains_frequency': {
        'cmd_read_register': (203, 2, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Mains Frequency',
        'unit': 'Hz',
    },
    'mains_power': {
        'cmd_read_register': (204, 0, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Average mains power',
        'unit': 'W',
    },
    'inverter_voltage': {
        'cmd_read_register': (205, 1, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Effective inverter voltage',
        'unit': 'V',
    },
    'inverter_current': {
        'cmd_read_register': (206, 1, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Effective inverter current',
        'unit': 'A',
    },
    'inverter_frequency': {
        'cmd_read_register': (207, 2, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Inverter frequency',
        'unit': 'Hz',
    },
    'inverter_power': {
        'cmd_read_register': (208, 0, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Average inverter power',
        'unit': 'W',
    },
    'inverter_average_charging_current': {
        'cmd_read_register': (233, 1, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Inverter charging average current',
        'unit': 'A',
    },
    'pv_average_charging_current': {
        'cmd_read_register': (234, 1, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'PV charging average current',
        'unit': 'A',
    },
    'inverter_charging_power': {
        'cmd_read_register': (209, 0, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Inverter charging power',
        'unit': 'W',
    },
    'output_voltage': {
        'cmd_read_register': (210, 1, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Output effective voltage',
        'unit': 'V',
    },
    'output_current': {
        'cmd_read_register': (211, 1, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Output effective Current',
        'unit': 'A',
    },
    'output_frequency': {
        'cmd_read_register': (212, 2, 3, False),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Output frequency',
        'unit': 'Hz',
    },
    'output_power': {
        'cmd_read_register': (213, 0, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Output active power',
        'unit': 'W',
    },
    'output_apparent_power': {
        'cmd_read_register': (214, 0, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Output apparent power',
        'unit': 'VA',
    },
    'temp_dc_dc': {
        'cmd_read_register': (226, 0, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'DC/DC Temperature',
        'unit': 'C',
    },
    'temp_inverter': {
        'cmd_read_register': (227, 0, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Inverter Temperature',
        'unit': 'C',
    },
    'battery_soc': {
        'cmd_read_register': (229, 0, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Battery State of Charge',
        'unit': '%',
    },
    'load_percentage': {
        'cmd_read_register': (225, 0, 3, True),
        'cmd_read_registers': (),
        'result_type': 'i16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Load percentage',
        'unit': '%',
    },
    'working_mode': {
        'cmd_read_register': (201, 0, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {0: 'Power On Mode', 1: 'Standby mode', 2: 'Mains mode', 3: 'Off-Grid mode', 4: 'Bypass mode',
                        5: 'Charging mode', 6: 'Fault mode'},
        'result_bits': {},
        'description': 'Working Mode',
        'unit': '-',
    },
    'fault_code': {
        'cmd_read_register': (),
        'cmd_read_registers': (100, 2, 3),
        'result_type': 'u32',
        'result_length': 2,
        'result_enum': {0: "---",
                        1: "Over temperature of inverter module",
                        2: "Over temperature of DCDC module",
                        3: "Battery over voltage",
                        4: "Over temperature of PV module",
                        5: "Output short circuited",
                        6: "Over Inverter voltage",
                        7: "Output over load",
                        8: "Bus over voltage",
                        9: "Bus soft start times out",
                        10: "PV over current",
                        11: "PV over voltage",
                        12: "Battery over current",
                        13: "Inverter over current",
                        14: "Bus low voltage",
                        15: "Reserve",
                        16: "Inverter DC component is too high",
                        17: "Reserve",
                        18: "The zero bias of Output current is too large",
                        19: "The zero bias of inverter current is too large",
                        20: "The zero bias of battery current is too large",
                        21: "The zero bias of PV current is too large",
                        22: "Inverter low voltage",
                        23: "Inverter negative power protection",
                        24: "The host in the parallel system is lost",
                        25: "Synchronization signal abnormal in the parallel system",
                        26: "The battery type is incompatible",
                        27: "Parallel versions are incompatible"},
        'result_bits': {},
        'description': 'Fault code',
        'unit': '-',
    },
    'warning_code': {
        'cmd_read_register': (),
        'cmd_read_registers': (108, 2, 3),
        'result_type': 'u32',
        'result_length': 2,
        'result_enum': {},
        'result_bits': {
            0: "Reserve",
            1: "Mains waveform abnormal",
            2: "Reserve",
            3: "Mains low voltage",
            4: "Mains over frequency",
            5: "Mains low frequency",
            6: "PV low voltage",
            7: "Over temperature",
            8: "Battery low voltage",
            9: "Battery is not connected",
            10: "Overload",
            11: "Battery Eq charging",
            12: "Battery is discharged at a low voltage and it has not been charged back to the recovery point",
            13: "Output power derating",
            14: "Fan blocked",
            15: "PV energy is too low to be use",
            16: "Parallel communication interrupted",
            17: "Output mode of Single and Parallel systems is inconsistent",
            18: "Battery voltage difference of parallel system is too large",
            19: "Reserve",
            20: "Reserve",
            21: "Reserve",
            22: "Reserve",
            23: "Reserve",
            24: "Reserve",
            25: "Reserve",
            26: "Reserve",
            27: "Reserve",
            28: "Reserve",
            29: "Reserve",
            30: "Reserve",
            31: "Reserve",
        },
        'description': 'Warning code',
        'unit': '-',
    },
    'series_no': {
        'cmd_read_register': (),
        'cmd_read_registers': (186, 12, 3),
        'result_type': 'char',
        'result_length': 12,
        'result_enum': {},
        'result_bits': {},
        'description': 'Series NO.',
        'unit': '-',
    },
    'rated_power': {
        'cmd_read_register': (643, 0, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Rated Power',
        'unit': 'W',
    },
    #
    'output_mode': {
        'cmd_read_register': (300, 0, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {0: "Single",
                        1: "Parallel",
                        2: "3 Phase-P1",
                        3: "3 Phase-P2",
                        4: "3 Phase-P3",
                        },
        'result_bits': {},
        'description': 'Output mode',
        'unit': '-',
    },
    'output_priority': {
        'cmd_read_register': (301, 0, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {0: "Utility-PV-Battery",
                        1: "PV-Utility-Battery",
                        2: "PV-Battery-Utility",
                        },
        'result_bits': {},
        'description': 'Output priority',
        'unit': '-',
    },
    'input_voltage_range': {
        'cmd_read_register': (302, 0, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {0: "Wide range",
                        1: "Narrow range",
                        },
        'result_bits': {},
        'description': 'Input voltage range',
        'unit': '-',
    },
    'buzzer_mode': {
        'cmd_read_register': (303, 0, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {0: "Mute in all situations",
                        1: "Sound when the input source is changed or there is a specific warning or fault",
                        2: "Sound when there is a specific warning or fault",
                        3: "Sound when fault occurs",
                        },
        'result_bits': {},
        'description': 'Buzzer mode',
        'unit': '-',
    },
    'lcd_backlight': {
        'cmd_read_register': (305, 0, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {0: "Timed off",
                        1: "Always on",
                        },
        'result_bits': {},
        'description': 'LCD backlight',
        'unit': '-',
    },
    'lcd_return_home': {
        'cmd_read_register': (306, 0, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {0: "Do not return automatically",
                        1: "Automatically return after 1 minute",
                        },
        'result_bits': {},
        'description': 'LCD automatically returns to the homepage',
        'unit': '-',
    },
    'energy_saving_mode': {
        'cmd_read_register': (307, 0, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {0: "Energy-saving mode is off",
                        1: "Energy-saving mode is on"
                        },
        'result_bits': {},
        'description': 'Energy-saving mode',
        'unit': '-',
    },
    'overload_automatic_restart': {
        'cmd_read_register': (308, 0, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {0: "Overload failure will not restart",
                        1: "Automatic restart after overload failure",
                        },
        'result_bits': {},
        'description': 'Overload automatic restart',
        'unit': '-',
    },
    'over_temperature_automatic_restart': {
        'cmd_read_register': (309, 0, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {0: "Over temperature failure will not restart",
                        1: "Automatic restart after over-temperature fault", },
        'result_bits': {},
        'description': 'Over temperature automatic restart',
        'unit': '-',
    },
    'overload_transfer_to_bypass': {
        'cmd_read_register': (310, 0, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {0: "Disable",
                        1: "Enable", },
        'result_bits': {},
        'description': 'Overload transfer to bypass enabled',
        'unit': '-',
    },
    'battery_eq_mode': {
        'cmd_read_register': (313, 0, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {0: "Disable",
                        1: "Enable", },
        'result_bits': {},
        'description': 'Battery Eq mode is enabled',
        'unit': '-',
    },
    'output_voltage_rw': {
        'cmd_read_register': (320, 1, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Output voltage',
        'unit': 'V',
    },
    'output_frequency_rw': {
        'cmd_read_register': (321, 2, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Output frequency',
        'unit': 'Hz',
    },
    'battery_overvoltage_protection_point': {
        'cmd_read_register': (323, 1, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Battery overvoltage protection point',
        'unit': 'V',
    },
    'max_charging_voltage': {
        'cmd_read_register': (324, 1, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Max charging voltage',
        'unit': 'V',
    },
    'floating_charging_voltage': {
        'cmd_read_register': (325, 1, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Floating charging voltage',
        'unit': 'V',
    },
    'battery_discharge_recovery_point_in_mains_mode': {
        'cmd_read_register': (326, 1, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Battery discharge recovery point in mains mode',
        'unit': 'V',
    },
    'battery_low_voltage_protection_point_in_mains_mode': {
        'cmd_read_register': (327, 1, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Battery low voltage protection point in mains mode',
        'unit': 'V',
    },
    'battery_low_voltage_protection_point_in_off-grid_mode': {
        'cmd_read_register': (329, 1, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Battery low voltage protection point in off-grid mode',
        'unit': 'V',
    },
    'battery_charging_priority': {
        'cmd_read_register': (331, 0, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {0: "Utility priority",
                        1: "PV priority", 2: "PV is at the same level as the Utility",
                        3: "Only PV charging is allowed", },
        'result_bits': {},
        'description': 'Battery charging priority',
        'unit': '-',
    },
    'maximum_charging_current': {
        'cmd_read_register': (332, 1, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Maximum charging current',
        'unit': 'A',
    },
    'maximum_mains_charging_current': {
        'cmd_read_register': (333, 1, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Maximum mains charging current',
        'unit': 'A',
    },
    'eq_charging_voltage': {
        'cmd_read_register': (334, 1, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Eq Charging voltage',
        'unit': 'V',
    },
    'bat_eq_time': {
        'cmd_read_register': (334, 0, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'bat_eq_time range:0-900',
        'unit': 'min',
    },
    'eq_timeout_exit': {
        'cmd_read_register': (336, 0, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Eq Timeout exit range:0-900',
        'unit': 'min',
    },
    'two_eq_charging_intervals': {
        'cmd_read_register': (337, 1, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {},
        'result_bits': {},
        'description': 'Two Eq charging intervals range:1-90',
        'unit': 'day',
    },
    'turn_on_mode': {
        'cmd_read_register': (406, 0, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {
            0: "Can be turn-on locally or remotely",
            1: "Only local turn-on",
            2: "Only remote turn-on"},
        'result_bits': {},
        'description': 'Turn on mode',
        'unit': '-',
    },
    'remote_switch': {
        'cmd_read_register': (420, 0, 3, False),
        'cmd_read_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {
            0: "Remote shutdown",
            1: "Remote turn-on",
        },
        'result_bits': {},
        'description': 'Remote switch',
        'unit': '-',
    },
    'exit_the_fault_mode': {
        'cmd_read_register': (),
        'cmd_read_registers': (),
        'cmd_write_register': (426, 0, 3, False),
        'cmd_write_registers': (),
        'result_type': 'u16',
        'result_length': 1,
        'result_enum': {
            1: "Remote turn-on",
        },
        'result_bits': {},
        'description': 'Exit the fault mode',
        'unit': '-',
    },
}


def print_register(register, name, vals):
    if (vals['result_type'] == 'u16' or vals['result_type'] == 'i16') and len(vals['result_enum']) > 0:
        if register < 0:
            print("{} - '{}':{} enum('error negative index')".format(name, vals['description'], register))
        else:
            print("{} - '{}':{} enum({})".format(name, vals['description'], register, vals['result_enum'][register]))
    else:
        print("{} - '{}':{} [{}]".format(name, vals['description'], register, vals['unit']))


def print_registers(registers, name, vals):
    if vals['result_type'] == 'char':
        registers_hex = ""
        for register in registers:
            registers_hex += hex(register >> 8) + ' ' + hex(register & 0xFF) + ' '
        print("{} - '{}':hex({})".format(name, vals['description'], registers_hex))
        registers_ascii = ""
        for register in registers:
            registers_ascii += chr(register >> 8) + ' ' + chr(register & 0xFF) + ' '
        print("{} - '{}':char({})".format(name, vals['description'], registers_ascii))
    elif (vals['result_type'] == 'u32' or vals['result_type'] == 'i32') and len(vals['result_enum']) > 0:
        registers_hex = ""
        for register in registers:
            registers_hex += hex(register >> 8) + ' ' + hex(register & 0xFF) + ' '
        int_signed = False
        if vals['result_type'] == 'i32':
            int_signed = True
        registers_int = int.from_bytes(registers, "big", signed=int_signed)
        if registers_int < 0:
            print("{} - '{}':hex({}) val({}) enum('error negative index')".format(name, vals['description'],
                                                                                  registers_hex, registers_int))
        else:
            print("{} - '{}':hex({}) val({}) enum({})".format(name, vals['description'], registers_hex, registers_int,
                                                              vals['result_enum'][registers_int]))
    elif (vals['result_type'] == 'u32') and len(vals['result_bits']) > 0:
        registers_hex = ""
        for register in registers:
            registers_hex += hex(register >> 8) + ' ' + hex(register & 0xFF) + ' '
        registers_int = int.from_bytes(registers, "big")
        registers_text = ""
        for n in range(32):
            if registers_int & (1 << n):
                registers_text += "'" + vals['result_bits'][n] + "' "
        print("{} - '{}':hex({}) val({}) bits({})".format(name, vals['description'], registers_hex, registers_int,
                                                          registers_text))
    else:
        print("{} - '{}':{} [{}]".format(name, vals['description'], registers, vals['unit']))


def test_read_example_with_values():
    instr.debug = False
    # instr.debug = True
    for name, vals in test_cmds.items():
        try:
            if len(vals['cmd_read_register']) > 0:
                register = instr.read_register(*vals['cmd_read_register'])
                print_register(register, name, vals)

            elif len(vals['cmd_read_registers']) > 0:
                registers = instr.read_registers(*vals['cmd_read_registers'])
                print_registers(registers, name, vals)

        except IOError:
            print("Failed to read from device - {}".format(name))
        except Exception as error:
            print(f"Exception {error=}, {type(error)=}")
            exit(1)


if __name__ == "__main__":
    try:
        instr = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
        instr.serial.baudrate = 9600
        instr.serial.parity = serial.PARITY_NONE
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
