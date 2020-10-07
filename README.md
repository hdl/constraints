# FPGA board constraints

Any HDL design targeting FPGA boards needs constraint files in a vendor/tool specific format. Constraints are typically tied to the board and the interfaces, but not to the actual design. Therefore, copying them is inefficient and increases the maintenance burden of projects including multiple designs to be tested on several boards. This repository provides constraint definitions in a standardised and distributed format, fot decoupling board details from design sources.

- Physical Constraints File (`*.pcf`) for Lattice IceCube2.
- Lattice Preference File (`*.lpf`) for Lattice Diamond.
- User Constraint Files (`*.ucf`) for Xilinx ISE ≤14.7.
- Xilinx Design Constraints (`*.xdc`) for Xilinx Vivado.
- Synopsis Design Constraints (`*.sdc`) for Altera Quartus-II.

## Short term goal

For each board, provide a set of constraint files, according to the following rules:

1. Split pin constrains from per IP core timing constrains.
2. Spilt pin constrains per interface/connector (switches, LEDs, Ethernet, UART, etc.). This allows enabling/disabling interfaces by selecting which files to include.
3. Prefix each port with the board name.
4. If an interface is fixed, include matching timing constraints. E.g. a button with `set_false_path`, `system_clock` with 100 MHz, or GMII with the 2 ns delay.

## Long term goal

- Define constraints in a YAML file with yet to be defined coding style rules.
- Write generators that export the content to vendor specific formats.
- Write importers that read existing vendor specific constraint files and generate a YAML file.

## Usage

The recommended approach for using these constraints in an existing HDL design is to define one top level source per board, on top of the design's top unit. To avoid ambiguity, we name the former `BoardTop` and the latter `DesignTop`. The purpose of BoardTop is describing board specific resources (PLLs, DCMs, RAM controllers, etc.) and type/polarity conversions, so that the DesignTop is unmodified for either simulation or implementation, with any tool and/or target board.

Find examples in the following repositories:

- [PLC2/Solution-StopWatch](https://github.com/PLC2/Solution-StopWatch)
- [eine/vhdl-cfg](https://github.com/eine/vhdl-cfg/)

## References

- [PoC](https://github.com/VLSI-EDA/PoC/) has a large collection of constraint files for Xilinx ISE/Vivado and Intel/Altera's Quartus-II. The initial commit of this repository imported most of the content from [VLSI-EDA/PoC: ucf/](https://github.com/VLSI-EDA/PoC/tree/master/ucf).
- [INTI-CMNB-FPGA/fpga_lib](https://github.com/INTI-CMNB-FPGA/fpga_lib) contains some YAML files that use a custom format: [INTI-CMNB-FPGA/fpga_lib: boards/](https://github.com/INTI-CMNB-FPGA/fpga_lib/tree/master/boards). A Python script ([boardfiles.py](https://github.com/INTI-CMNB-FPGA/fpga_lib/blob/master/scripts/boardfiles.py)) allows generating UCF files from the YAML sources.
- `*.pcf` and `*.lpf` files for open source boards were picked from [eine/vhdl-cfg](https://github.com/eine/vhdl-cfg/), which are based on resources from [ghdl/ghdl-yosys-plugin](https://github.com/ghdl/ghdl-yosys-plugin), [antonblanchard/ghdl-yosys-blink](https://github.com/antonblanchard/ghdl-yosys-blink), [im-tomu/fomu-workshop](https://github.com/im-tomu/fomu-workshop), etc.
- [olofk/fusesoc](https://github.com/olofk/fusesoc) proposes an open source YAML format for defining cores. Hence, the constrains provided in this repository are expected to be used in those core definition sources. Ideally, fusesoc might import the YAML definition, instead of defining different filesets for each tool.
