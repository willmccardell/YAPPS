#!/usr/bin/env python

import socket
import subprocess
import sys
from datetime import datetime


def main(targetHost):

    retVal = ''
    abortEarly = False
    try:
        translated_host = socket.gethostbyname(targetHost);
        retVal = translated_host
    except:
        retVal = f'Name {targetHost} not recognized. Aborting.'
        abortEarly = True


    print(retVal)
    if abortEarly:
        return retVal

    #do stuff here

    return retVal


#Not in use now that I'm using gethostbyname
def CheckIP(address):
    isValid = False
    try:
        isValid = socket.inet_aton(address)
    except:
        print(f'Isvalid: {isValid}')
        print(f'The address: {address}')
    return isValid


if __name__ == '__main__':
     main(sys.argv[1])