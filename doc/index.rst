.. include:: shields.inc

The FPGA Board Constraints Documentation
########################################

.. image:: _static/banner.png
   :height: 90 px
   :align: center
   :target: https://github.com/hdl/constraints

.. raw:: html

    <br>

.. centered:: |SHIELD:svg:gh:hdl:constraints| |SHIELD:svg:gh:hdl:packages| |SHIELD:svg:gh:hdl:awesome| |SHIELD:svg:Reports-gitter|

Hardware Description Language (HDL) designs prototyped on FPGAs are constrained by the devices and interfaces available
on the development boards.
Most of the constraints are tied to the physical characteristics and not to the logic design.
Therefore, the maintenance burden of projects to be tested on multiple boards can be reduced by sharing constraint
definition files.
This repository provides constraint definitions in a standardised and distributed format, for decoupling board details
from design sources.
Unlike other similar solutions, these resources are not tied to any specific project management tool.

On top of pinout and I/O constraints, programming/configuring development boards implies dealing with external memories
(either flash or SDRAM) and typically debugging the SoC designs using JTAG, GDB, etc. Hence, this repository also
contains data about those.

.. toctree::

   Structure
   Usage
   Contributing
   Attributes
   Similar
   ProgDebug

.. toctree::
   :caption: Data
   :maxdepth: 1

   Data/Boards/index
   Data/Devices
   Data/Flash
   Data/SDRAM
