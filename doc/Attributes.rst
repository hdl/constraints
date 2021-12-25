HDL attributes/annotations
##########################

Some tools/vendors support specifying implementation constraints through attributes/annotations in HDL sources.

VHDL
====

* Timing

  * Specify SDC timing constraints inside a module
  * Setting cross-clock options
  * Disable optimizations like shiftregister extraction

* Physical

  * Setting pin locations

* Encoding

  * FSM encoding
  * Type/enum encoding

* Disable renaming optimization so a wire can be used for debugging

  * Attach a logic analyzer

* Translation hints

  * Setting memory styles (register, distributedRAM/LUTRAM, BlockRAM, UltraRAM, ...)

Verilog
=======

See :ref:`yosys-symbiflow-plugin <Similar:yosys-symbiflow-plugins>`.
