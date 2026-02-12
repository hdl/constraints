.. _Similar:

Similar resources
#################

.. _Similar:PoC:

VLSI-EDA/PoC
============

:ghrepo:`PoC <VLSI-EDA/PoC>` has a large collection of constraint files for Xilinx ISE/Vivado and Intel/Altera's
Quartus-II.
The initial commit of this repository imported most of the content from
:ghrepo:`VLSI-EDA/PoC: ucf/ <VLSI-EDA/PoC/tree/master/ucf>`.

.. _Similar:fpga_lib:

INTI-CMNB-FPGA/fpga_lib
=======================

:ghrepo:`fpga_lib <INTI-CMNB-FPGA/fpga_lib>` contains some YAML files that use a custom format:
:ghrepo:`INTI-CMNB-FPGA/fpga_lib: boards/ <INTI-CMNB-FPGA/fpga_lib/tree/master/boards>`.
A Python script (:ghrepo:`boardfiles.py <INTI-CMNB-FPGA/fpga_lib/blob/master/scripts/boardfiles.py>`) allows generating
UCF files from the YAML sources.

.. _Similar:ghdl-yosys-plugin:

ghdl/ghdl-yosys-plugin
======================

Constraints files (`.pcf` and `.lpf`) for open source boards are based on resources from
:ghrepo:`ghdl/ghdl-yosys-plugin`,
:ghrepo:`antonblanchard/ghdl-yosys-blink`,
:ghrepo:`im-tomu/fomu-workshop`, etc.

.. _Similar:litex-boards:

litex-hub/litex-boards
======================

:ghrepo:`litex-boards <litex-hub/litex-boards>` is equivalent to this repository, but constraints are defined as Python
modules.
It'd be interesting to allow conversions between the YAML and LiteX board definitions.
At the same time, from LiteX definitions it should be possible to generate vendor constraint files matching the guidelines.

.. _Similar:amaranth-boards:

amaranth-lang/amaranth-boards
=============================

:ghrepo:`amaranth-lang/amaranth-boards` provides board and connector definition files for Amaranth HDL.
It is also equivalent to this repository, but constraints are defined as Python modules.
As with litex-boards, it'd be interesting to allow conversions between the YAML and Amaranth HDL board definitions.
The syntax used in amaranth-boards feels more streamlined.

.. _Similar:yosys-symbiflow-plugins:

SymbiFlow/yosys-symbiflow-plugins
=================================

:ghrepo:`yosys-symbiflow-plugins <SymbiFlow/yosys-symbiflow-plugins>` contains plugins for Yosys developed as
part of the :ghrepo:`SymbiFlow` project.
Some of those plugins are the ``xdc-plugin`` or the ``sdc-plugin``.
Those take the constraints and information and converts them to annotations on RTL.
Annotations can also be directly provided in HDL too.
Hence, the aim is to collect everything into the RTL and then write the data back for downstream tools to use.
The main benefit of this approach is using the names in RTL, instead of dealing with mangled names after optimisation.
See also `XDC commands supported by SymbiFlow Yosys Plugins <https://docs.google.com/spreadsheets/d/1G-E2Dq8YG4g9Z6mTygpumwlI_vNlFUQinc9gMgePfec>`__
and `Yosys and Constraints System <https://docs.google.com/drawings/d/1r2LXypJF5AD40LfHegml3_fIvPT2jZ3n2OZYW9-9dLU>`__.

.. _Similar:fusesoc:

olofk/fusesoc
=============

:ghrepo:`fusesoc <olofk/fusesoc>` proposes an open source YAML format for defining cores.
Hence, the constrains provided in this repository are expected to be used in those core definition sources.
Ideally, fusesoc might import the YAML definition, instead of defining different filesets for each tool.

See also `olofk/corescore: data <https://github.com/olofk/corescore/tree/master/data>`__.

.. _Similar:XilinxBoardStore:

Xilinx/XilinxBoardStore
=======================

The board data files used with Xilinx Vivado are hosted at
:ghrepo:`Xilinx/XilinxBoardStore`.
The upstream of :ghrepo:`Xilinx/XilinxBoardStore: boards/Digilent/ <Xilinx/XilinxBoardStore/tree/master/boards/Digilent>`
is :ghrepo:`Digilent/vivado-boards`.
