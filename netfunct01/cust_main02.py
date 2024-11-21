#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

# python3 -m pip install crayons
import crayons

# function to push commands
def commandpush(devicereboot): # devicecmd==dict

    for ip in devicereboot.keys(): # looping through the dict
        print(f'{crayons.green("Connecting to")}.. {ip} is {crayons.red("REBOOTING NOW!")}')
            # we'll learn to write code that sends cmds to device here
    return None

# start our main script
def main():
    """called at runtime"""

    # dict containing IPs mapped to a list of physical interfaces and their state
    devicereboot = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print(f"Welcome to the {crayons.blue('network')} device rebooter.") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicereboot) # call function to push commands to devices

# call our main function
main()

