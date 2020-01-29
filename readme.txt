Printsum 
===
#### (as in the helicopter scene in Full Metal Jacket)

*This document is markdown formatted*

## What is it?
Printsum is a Python utility to aggregate the statistics provided by Simplify3D. Printsum is still in the MVP development stage, so there's currently no external output / graphing. 
The aim is to eventually interface with a web interface (likely with PowerBI or similar).

## Assumptions 
I have a regular workflow where I:
- export the STL to a root folder
- drop the STL into Simplify3D and generate the gcode to a child folder according to the printer and material type (ie Sidewinder PLA)
- send the gcode file to either Octoprint or USB drive and print the file.
- once the print is complete, either move the gcode to a child folder of the above folder (ie Sidewinder PLA Printed or Sidewinder PLA Test Prints)


