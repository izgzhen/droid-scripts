#!/usr/bin/env python3

import sys
import os

WORKDIR = "/usr/src/tools"
APK = sys.argv[1]
assert APK.startswith("apks/")
APKNAME = os.path.basename(APK)
PWD = os.getcwd()

OUTPUT = WORKDIR + "/output"
DARE_OUTPUT = OUTPUT + "/dare"
APK = APK.replace("apks/", WORKDIR + "/apks/")
PATH_LOGS = DARE_OUTPUT + "/logs"
DARE_RESULTS = DARE_OUTPUT + "/results"
RETARGETED_PATH = DARE_RESULTS + "/retargeted"

cmd = "docker run --rm --memory=1gb " + \
  f"-v {PWD}/output:{OUTPUT} " + \
  f"-v {PWD}/apks:{WORKDIR}/apks " + \
  f"-t izgzhen/droid-scripts /bin/bash -c " + \
  f'"mkdir -p {PATH_LOGS}; ./dare/dare -d {DARE_RESULTS} {APK} > {PATH_LOGS}/{APKNAME}-dare.txt"'

print(cmd)
os.system(cmd)
