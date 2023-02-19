# TheLodgeGallery

## Build:
`./build.sh`

## Run:
`sudo -s ./start.sh`

## Usage:
* Connect to zmq REQ socket on rasbpi port 5555
* Send JSON action message that fulfils schema in `schema/matrix_action.json`
* Currently only support `fill_colour` action
* Example client in `examples/command_line_colours.py`