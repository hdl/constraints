# Digital IO on PCIe edge connector (Rev.D and newer)

set_property PACKAGE_PIN K2 [get_ports PicoEVB_GPIO_DI[0]]
set_property PACKAGE_PIN K1 [get_ports PicoEVB_GPIO_DI[1]]
set_property PACKAGE_PIN V2 [get_ports PicoEVB_GPIO_DO[0]]
set_property PACKAGE_PIN V3 [get_ports PicoEVB_GPIO_DO[1]]

set_property IOSTANDARD LVCMOS33 [get_ports PicoEVB_GPIO_DI[0]]
set_property IOSTANDARD LVCMOS33 [get_ports PicoEVB_GPIO_DI[1]]
set_property IOSTANDARD LVCMOS33 [get_ports PicoEVB_GPIO_DO[0]]
set_property IOSTANDARD LVCMOS33 [get_ports PicoEVB_GPIO_DO[1]]
