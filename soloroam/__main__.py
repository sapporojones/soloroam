import argparse

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


import soloroam.run as run



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", help="Set output level of logging.  Disabled by default.")
    parser.add_argument(
        "-s", help="Set starting system.  Defaults to 6VDT-H.", default="6VDT-H"
    )
    parser.add_argument(
        "-d", help="Set destination system.  Defaults to OWXT-5.", default="OWXT-5"
    )
    args = parser.parse_args()
    run.handler(args)
