set_property PACKAGE_PIN V14 [get_ports {PicoEVB_GPIO_LED[2]}]
set_property PACKAGE_PIN V13 [get_ports {PicoEVB_GPIO_LED[1]}]
set_property PACKAGE_PIN V12 [get_ports {PicoEVB_GPIO_LED[0]}]

set_property IOSTANDARD LVCMOS33 [get_ports {PicoEVB_GPIO_LED[2]}]
set_property IOSTANDARD LVCMOS33 [get_ports {PicoEVB_GPIO_LED[1]}]
set_property IOSTANDARD LVCMOS33 [get_ports {PicoEVB_GPIO_LED[0]}]

set_property PULLUP true [get_ports {PicoEVB_GPIO_LED[2]}]
set_property PULLUP true [get_ports {PicoEVB_GPIO_LED[1]}]
set_property PULLUP true [get_ports {PicoEVB_GPIO_LED[0]}]

set_property DRIVE 8 [get_ports {PicoEVB_GPIO_LED[2]}]
set_property DRIVE 8 [get_ports {PicoEVB_GPIO_LED[1]}]
set_property DRIVE 8 [get_ports {PicoEVB_GPIO_LED[0]}]
