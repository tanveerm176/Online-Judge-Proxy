#!/usr/bin/env python
import sys
from pathlib import Path
from KattisClient import KattisClient

def main():

    kattisCLI = KattisClient()
    print(kattisCLI.cookies)
    
    return


if __name__ == '__main__':
    main()