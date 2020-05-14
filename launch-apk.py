#!/usr/bin/env python3

import glob
import sys
import os

from msbase.utils import getenv, load_json, write_pretty_json, log_progress
from msbase.subprocess_ import try_call_std

BUILD_TOOLS = os.getenv("BUILD_TOOLS")

def extract_in_quotes(l):
    s = l[l.find("'")+1:]
    s = s[:s.find("'")]
    return s

def get_default():
    return {"uses-permissions": [], "application-label": None, "package": None, "launchable": None}

def aapt(cmd, apk):
    if cmd in ["label", "package", "launch"]:
        stdout, _, code = try_call_std([BUILD_TOOLS + "/aapt", "dump", "badging", apk], noexception=True, output=False, print_cmd=False)
        if code == 0:
            for l in stdout.splitlines():
                if l.startswith("application-label:"):
                    label = extract_in_quotes(l)
                if l.startswith("package: name="):
                    package = extract_in_quotes(l)
                if l.startswith("launchable-activity: name="):
                    launchable = extract_in_quotes(l)
        if cmd == "label":
            print(label)
        if cmd == "package":
            print(package)
        if cmd == "launch":
            try_call_std(["adb", "shell", "am", "start", "-n", package + "/" + launchable])

    if cmd == "permissions":
        permissions = []
        stdout, _, code = try_call_std([BUILD_TOOLS + "/aapt", "dump", "permissions", apk], noexception=True)
        if code == 0:
            for l in stdout.splitlines():
                if l.startswith("uses-permission: name="):
                    permissions.append(extract_in_quotes(l))
        print(permissions)

if __name__ == "__main__":
    aapt(sys.argv[1], sys.argv[2])