#!/usr/bin/env python

import os
import sys
from distutils.version import StrictVersion

def get_version_file():
    for root, dirs, files in os.walk("."):
        for f in files:
            if f == "VERSION":
                return os.path.join(os.path.abspath(root), f)

    new_file = os.path.join(os.path.abspath("."), "VERSION")
    open(new_file, "w").close()
    return new_file

def get_version(version_string):
    if not version_string:
        version_string = "0.0.0"
    v = StrictVersion(version_string.strip())
    return v

def inc_by(base, by):
    print "Incrementing %s by %s" % (base, by)
    return map(sum, zip(base.version, by.version))

if __name__ == "__main__":

    inc_version = get_version(sys.argv[1] if len(sys.argv) > 1 else "0.1.0")

    version_file = get_version_file()

    with open(version_file) as fp:
        current = get_version(fp.read())
        print "Current Version: %s" % current

    with open(version_file, "w") as fp:
        new_version = ".".join(map(str, inc_by(current, inc_version)))
        print "New Version: %s" % new_version
        fp.write("%s\n" % new_version)
