# repetier-wrapper
RepetierHost 2.1.3 doesn't work with PrusaSlicer as Prusa has changed the command line behavior.  
RepetierHost expect to launch the graphical interface using --gui but on PrusaSlicer it's the default, and slices with --slice.

## To install
- copy repetier-wrapper.py in the prusa-slicer binary directory
- point to repetier-wrapper.py instead of prusa-slicer binary in Repetier-Host

Requires Python3.  
Tested on Linux. Likely working on macOS.  
Tested with v.2.0.0 of Prusa Slicer  https://github.com/prusa3d/PrusaSlicer/releases
