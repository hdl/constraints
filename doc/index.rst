The FPGA Board Constraints Documentation
########################################

.. image:: _static/banner.png
   :height: 90 px
   :align: center
   :target: https://github.com/hdl/constraints

.. raw:: html

    <br>

..
  https://github.com/hdl/constraints[image:https://img.shields.io/badge/hdl-constraints-f2f1ef.svg?longCache=true&style=flat-square&logo=GitHub&logoColor=f2f1ef[title='hdl/constraints GitHub repository']]
  https://github.com/hdl/packages[image:https://img.shields.io/badge/hdl-packages-f2f1ef.svg?longCache=true&style=flat-square&logo=GitHub&logoColor=f2f1ef[title='hdl/packages GitHub repository']] |
  https://gitter.im/hdl/community[image:https://img.shields.io/gitter/room/hdl/community.svg?longCache=true&style=flat-square&logo=gitter&logoColor=fff&color=4db797[title='hdl/community on gitter.im']] |
  https://github.com/hdl/awesome[image:https://img.shields.io/badge/hdl-awesome-f2f1ef.svg?longCache=true&style=flat-square&logo=GitHub&logoColor=f2f1ef[title='hdl/awesome GitHub repository']]

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
