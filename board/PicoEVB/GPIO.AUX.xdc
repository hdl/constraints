# Connector pins 1, 2, 4 and 5, respectively.
# May be re-purposed to use with XADC.

set_property PACKAGE_PIN A14 [get_ports PicoEVB_GPIO_AUX[0]]
set_property PACKAGE_PIN A13 [get_ports PicoEVB_GPIO_AUX[1]]
set_property PACKAGE_PIN B12 [get_ports PicoEVB_GPIO_AUX[2]]
set_property PACKAGE_PIN A12 [get_ports PicoEVB_GPIO_AUX[3]]

set_property IOSTANDARD LVCMOS33 [get_ports PicoEVB_GPIO_AUX[0]]
set_property IOSTANDARD LVCMOS33 [get_ports PicoEVB_GPIO_AUX[1]]
set_property IOSTANDARD LVCMOS33 [get_ports PicoEVB_GPIO_AUX[2]]
set_property IOSTANDARD LVCMOS33 [get_ports PicoEVB_GPIO_AUX[3]]
