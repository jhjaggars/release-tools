#!/usr/bin/env python

import os
import argparse
import sys
import subprocess
import requests

if __name__ == "__main__":

    p = argparse.ArgumentParser()
    p.add_argument("url")
    p.add_argument("repositories")
    args = p.parse_args()

    rep = requests.get(args.url)
    for project, details in rep.json()["versions"].items():
        os.chdir(os.path.join(args.repositories, project))
        subprocess.call("git remote update", shell=True)
        push = raw_input("Tag %s:%s with %s? " % (project, details["version"], details["commit"]))
        if push.lower() == "y":
            subprocess.call("git tag %s %s" % (details["version"], details["commit"]), shell=True)
            subprocess.call("git push --tags", shell=True)
