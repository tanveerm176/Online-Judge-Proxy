#!/usr/bin/env python
import sys
from pathlib import Path
from KattisClient import KattisClient
import argparse
import os

#note: do we want this to be cont. running
def main():
    kattis = KattisClient()

    #create parser
    parser = argparse.ArgumentParser(prog='Online Judge Proxy', description='Submit a solution to Kattis, CodeForces, or LeetCode')

    #TODO: need to add fucntionality for this flag
    parser.add_argument('-c','--client', help="which client to use")

    parser.add_argument("problemID", help="Enter the problem ID", type=str)

    #TODO: increase number of files 
    parser.add_argument("files", nargs='+')

    args = parser.parse_args()

    files = args.files
    files = sorted(list(set(args.files)))

    # problemName = kattis.get_problem_name(files)
    problemID = args.problemID

    kattis.submit_problem(problemID, files=files)
    return


if __name__ == '__main__':
    main()