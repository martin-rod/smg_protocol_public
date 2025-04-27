# smg-ii / smg-iii

Monitor a ISolar/EASUN SMG II inverter via RS232

## References

* https://powerforum.co.za/topic/11341-i-want-to-know-protocol-used-in-isolar-smg-ii-5kw/
* https://github.com/syssi/esphome-smg-ii
* https://github.com/shakthisachintha/SRNE-Hybrid-Inverter-Monitor.git

## Supported devices

* ISolar SMG II - not tested (from syssi/esphome-smg-ii)
* EASUN SMG II - not tested (from syssi/esphome-smg-ii)
* PowMr POW-HVM5.5K-48V / POW-HVM5.5K-48V-P - not tested (from syssi/esphome-smg-ii)
* iSolar SMG-III-6.2kW - tested

## Requirements

* RS232 to USB

## Schematics

```
               RS232
┌──────────┐              ┌──────────┐
│          │              │          │
│          │<---- TX ---->│  RS232   │
│  SMG     │<---- RX ---->│  to USB  │
│          │<---- GND --->│  module  │
│          │              │          │
└──────────┘              └──────────┘
```

### RJ45 jack

| Pin     | Purpose      | Color T-568B |
| :-----: | :----------- | :------------|
|    1    | TX           | White-Orange |
|    2    | RX           | Orange       |
|    3    |              |              |
|    4    | VCC 12V      | Blue         |
|    5    |              |              |
|    6    |              |              |
|    7    |              |              |
|    8    | GND          | Brown        |

Please be aware of the different RJ45 pinout colors ([T-568A vs. T-568B](images/rj45-colors-t568a-vs-t568.png)).

## Protocol

The protocol is Modbus RTU via RS232.

| Description                                            | Unit     |  Res  | Addr | Len | R/W | Values |
| -----------------------------------------------------: | -------: |  ---: | :--: | :-: | :-: | :----- |
| Fault code                                             |          | ULong |  100 |  2  |  R  | |
| Warning code                                           |          | ULong |  108 |  2  |  R  | |
| Serial number                                          |          | Ascii |  186 | 12  |  R  | |
| Operation Mode                                         |          |  UInt |  201 |  1  |  R  | 0: Power On<br>1: Standby<br>2: Mains<br>3: Off-Grid<br>4: Bypass<br>5: Charging<br>6: Fault |
| Effective mains voltage                                |  0.1V    |  Int  |  202 |  1  |  R  | |
| Mains Frequency                                        |  0.01Hz  |  Int  |  203 |  1  |  R  | |
| Average mains power                                    |  1W      |  Int  |  204 |  1  |  R  | |
| Effective inverter voltage                             |  0.1V    |  Int  |  205 |  1  |  R  | |
| Effective inverter current                             |  0.1A    |  Int  |  206 |  1  |  R  | |
| Inverter frequency                                     |  0.01Hz  |  Int  |  207 |  1  |  R  | |
| Average inverter power                                 |  1W      |  Int  |  208 |  1  |  R  | Positive numbers indicate inverter output<br>Negative numbers indicate inverter input |
| Inverter charging power                                |  1W      |  Int  |  209 |  1  |  R  | |
| Output effective voltage                               |  0.1V    |  Int  |  210 |  1  |  R  | |
| Output effective Current                               |  0.1A    |  Int  |  211 |  1  |  R  | |
| Output frequency                                       |  0.01Hz  |  Int  |  212 |  1  |  R  | |
| Output active power                                    |  1W      |  Int  |  213 |  1  |  R  | |
| Output apparent power                                  |  1VA     |  Int  |  214 |  1  |  R  | |
| Battery average voltage                                |  0.1V    |  Int  |  215 |  1  |  R  | |
| Battery average Current                                |  0.1A    |  Int  |  216 |  1  |  R  | |
| Battery average power                                  |  1W      |  Int  |  217 |  1  |  R  | |
| PV average voltage                                     |  0.1V    |  Int  |  219 |  1  |  R  | |
| PV average Current                                     |  0.1A    |  Int  |  220 |  1  |  R  | |
| PV average power                                       |  1W      |  Int  |  223 |  1  |  R  | |
| PV charging average power                              |  1W      |  Int  |  224 |  1  |  R  | |
| Load percentage                                        |  1%      |  Int  |  225 |  1  |  R  | |
| DCDC Temperature                                       |  1°C     |  Int  |  226 |  1  |  R  | |
| Inverter Temperature                                   |  1°C     |  Int  |  227 |  1  |  R  | |
| Battery state of charge                                |  1%      |  UInt |  229 |  1  |  R  | |
| Battery average current                                |  0.1A    |  Int  |  232 |  1  |  R  | Positive number means charging<br>Negative number means discharging |
| Inverter charging average current                      |  0.1A    |  Int  |  233 |  1  |  R  | |
| PV charging average current                            |  0.1A    |  Int  |  234 |  1  |  R  | |
| Output Mode                                            |          |  Uint |  300 |  1  | R/W | 0: Single<br>1: Parallel<br>2: 3 Phase-P1<br>3: 3 Phase-P2<br>4: 3 Phase-P3 |
| Output priority                                        |          |  Uint |  301 |  1  | R/W | 0: Utility-PV-Battery<br>1: PV-Utility-Battery<br>2: PV-Battery-Utility  |
| Input voltage range                                    |          |  Uint |  302 |  1  | R/W | 0: Wide range<br>1: Narrow range                                         |
| Buzzer mode                                            |          |  Uint |  303 |  1  | R/W | 0: Mute in all situations<br>1: Sound when the input source is changed or there is a specific warning or fault<br>2: Sound when there is aspecific warning or fault<br>3: Sound when fault occurs |
| LCD backlight                                          |          |  Uint |  305 |  1  | R/W | 0: Timed off<br>1: Always on                                             |
| LCD automatically returns to the homepage              |          |  Uint |  306 |  1  | R/W | 0: Do not return automatically<br>1: Automatically return after 1 minute |
| Energy-saving mode                                     |          |  Uint |  307 |  1  | R/W | 0: Energy-saving mode is off<br>1: Energy-saving mode is on              |
| Overload automatic restart                             |          |  Uint |  308 |  1  | R/W | 0: Overload failure will not restart<br>1: Automatic restart after overload failure |
| Over temperature automatic restart                     |          |  Uint |  309 |  1  | R/W | 0: Over temperature failure will not restart<br>1: Automatic restart after over-temperature fault |
| Overload transfer to bypass enabled                    |          |  Uint |  310 |  1  | R/W | 0: Disable<br>1: Enable                                                  |
| Battery Eq mode is enabled                             |          |  Uint |  313 |  1  | R/W | 0: Disable<br>1: Enable                                                  |
| Output voltage                                         |  0.1V    |  Uint |  320 |  1  | R/W | |
| Output frequency                                       |  0.01Hz  |  Uint |  321 |  1  | R/W | |
| Battery overvoltage protection point                   |  0.1V    |  Uint |  323 |  1  | R/W | |
| Max charging voltage                                   |  0.1V    |  Uint |  324 |  1  | R/W | |
| Floating charging voltage                              |  0.1V    |  Uint |  325 |  1  | R/W | |
| Battery discharge recovery point in mains mode         |  0.1V    |  Uint |  326 |  1  | R/W | |
| Battery low voltage protection point in mains mode     |  0.1V    |  Uint |  327 |  1  | R/W | |
| Battery low voltage protection point in off-grid mode  |  0.1V    |  Uint |  329 |  1  | R/W | |
| Battery charging priority                              |          |  Uint |  331 |  1  | R/W | 0: Utility priority<br>1: PV priority<br>2: PV is at the same level as the Utility<br>3: Only PV charging is allowed |
| Maximum charging current                               |  0.1A    |  Uint |  332 |  1  | R/W | |
| Maximum mains charging current                         |  0.1A    |  Uint |  333 |  1  | R/W | |
| Eq Charging voltage                                    |  0.1V    |  Uint |  334 |  1  | R/W | |
| Battery equalization time                              |  min     |  Uint |  335 |  1  | R/W | Range: 0~900 |
| Equalization timeout exit                              |  min     |  Uint |  336 |  1  | R/W | Range: 0~900 |
| Two equalization charging intervals                    |  day     |  Uint |  337 |  1  | R/W | Range: 1~90  |
| Turn on mode                                           |          |  Uint |  406 |  1  | R/W | 0: Can be turn-on locally or remotely<br>1: Only local turn-on<br>2: Only remote turn-on |
| Remote switch                                          |          |  Uint |  420 |  1  | R/W | 0: Remote shutdown<br>1: Remote turn-on |
| Exit the fault mode                                    |          |  Uint |  426 |     |  W  | 1: Exit the fault state (only when the inverter enters the fault mode, it could be available) |
| Rated Power                                            |  W       |  Uint |  643 |  1  |  R  | |
