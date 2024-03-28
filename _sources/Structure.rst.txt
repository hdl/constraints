.. _Structure:

Structure of the repository
###########################

* ``board/``: a subdir for each board

  * ``<BOARDNAME>``:

    * ``info.yml`` or ``info.md``: board data
    * ``<CONSTRAINT_FILE(S)>``

* ``device/``: a subdir for each device

  * ``<DEVICENAME>``

    * ``info.yml``: device data


Types of constraint files:

* Physical Constraints File (``*.pcf``) for Lattice IceCube2.
* Lattice Preference File (``*.lpf``) for Lattice Diamond.
* User Constraint Files (``*.ucf``) for Xilinx ISE ≤14.7.
* Xilinx Design Constraints (``*.xdc``) for Xilinx Vivado.
* Synopsis Design Constraints (``*.sdc``) for Intel Quartus Prime (formerly Altera Quartus-II).
* Physical Design Constraints (``*.pdc``) for Microsemi Libero-SoC.

For each board, sets of constraint files are provided according to the following rules:

* Split pin constrains from per IP core timing constrains.
* Group pin constrains per interface/connector (switches, LEDs, Ethernet, UART, etc.). This allows enabling/disabling interfaces by selecting which files to include.
* Use vectors/arrays for unnamed non-bidirectional ports, instead of numbering pins individually.
* Prefix each port with the board name.
* If an interface is fixed, include matching timing constraints. E.g. a button with ``set_false_path``, ``system_clock`` with 100 MHz, or GMII with the 2 ns delay.
* Postfix low-active signals with ``_n``.
