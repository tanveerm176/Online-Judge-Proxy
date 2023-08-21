import sys
from pathlib import Path
from .KattisClient import KattisClient
from .CodeforcesClient import CodeforcesClient
import argparse
import os


#note: do we want this to be cont. running
def main():
    cf = CodeforcesClient()

    kattis = KattisClient()

    #create parser
    parser = argparse.ArgumentParser(prog='Online Judge Proxy', description='Submit a solution to Kattis, CodeForces, or LeetCode')

    #TODO: need to add fucntionality for this flag
    parser.add_argument('-p','--platform', help="which platform to submit to")

    parser.add_argument("-id","--problemID", help="Enter the problem ID", type=str)

    parser.add_argument("file", nargs=1)

    args = parser.parse_args()

    platform = args.platform

    files = args.file
    files = sorted(list(set(args.file)))

    if not args.problemID:
        problemID = kattis.get_problem_id(files)
    else:
        problemID = args.problemID

    if platform == "codeforces":
        cf.submit(files[0], problemID)  
    
    else:
        kattis.submit_problem(problemID, files=files)

    return


if __name__ == '__main__':
    main()