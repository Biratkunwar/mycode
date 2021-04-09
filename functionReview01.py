#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

import json

# function to push commands
def commandpush(devicecmd): # devicecmd==list
    """runs the commands passed as devicecmd"""
    for coffeetime in devicecmd.keys():
        print('Handshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + mycmds )
            # we'll learn to write code that sends cmds to device here

def commandget(fileloc):
    """grabs the commands from a file passed in as fileloc"""
    with open(fileloc, "r") as cmdfile:
        # load the JSON file as python lists / dicts
        cmdstoissue = json.load(cmdfile)
    return cmdstoissue

# start our main script
def main():
    """runtime code"""
    fileloc = input("name of file to read commands from?")

    # call our function 'commandget()' and pass it the location of the file the
    # user wants to read from
    work2do = commandget(fileloc)

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(work2do) # call function to push commands to devices

# call our main function
main()
