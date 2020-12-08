# my-python-utils
Python command-line scripts that perform a variety of functions

PREREQUISITES
- Operating System: Mac OS X, Linux, Windows
- Software: Install Python3

NOTES: You'll need Python3 installed or these will not work. Plenty of tutorials on the net, but I may add some to the wiki in the future. In order to see command options/requirements, utilize the --help flag. Example: passwordgen.py --help or subnetcalc.py -h

PASSWORD GENERATOR
- Description: Generates a random password
- Executable: genpass.py
- Module (required): pass_module.py

SUBNET ID AND BROADCAST ADDRESS CALCULATOR
- Description: Takes an existing IPv4 address and subnet mask. Outputs the Subnet ID and Broadcast Address. This may come in handy for sys/net admins when attempting to figure out what network/subnet a device is on. The broadcast address is the last IP on a network/subnet, which may assist in calculating the range of IP addresses on the network/subnet

- Files: subnetcalcv4.py
