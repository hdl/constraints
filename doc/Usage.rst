Usage
=====

This repository is expected to be added as a git submodule or otherwise vendored in existing HDL designs.

The recommended approach is defining one top level source per board, on top of the design's top unit.
To avoid ambiguity, we name the former ``BoardTop`` and the latter ``DesignTop``.
The purpose of BoardTop is to describe board specific resources (PLLs, DCMs, RAM controllers, etc.) and type/polarity
conversions, so that the DesignTop is unmodified for either simulation or implementation, with any tool and/or for any
target board.

Responsibilities of a ``BoardTop`` component/module:

* Normalize low-active signals to high-active signals.
* I/O buffers, if needed.
* Input synchronization.
* Output flip-flops.
* Converting a tristate-bus (I, O, T) to a bi-directional inout signal (and bi-directional buffer).
* Debouncing and maybe edge-detection.

Find examples in the following repositories:

* :ghrepo:`PLC2/Solution-StopWatch`
* :ghrepo:`dbhi/vboard`

