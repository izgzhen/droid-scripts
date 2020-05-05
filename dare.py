#!/usr/bin/env python3

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
assert os.getcwd() == SCRIPT_DIR

WORKDIR = "/usr/src/tools"
APK = os.path.relpath(sys.argv[1])
SHA256SUM = sys.argv[2]
assert APK.startswith("apks/"), APK
APKNAME = os.path.basename(APK)
PWD = os.getcwd()

OUTPUT = WORKDIR + "/output"
DARE_OUTPUT = OUTPUT + "/dare"
APK = APK.replace("apks/", WORKDIR + "/apks/")
PATH_LOGS = DARE_OUTPUT + "/logs"
DARE_RESULTS = DARE_OUTPUT + "/" + SHA256SUM

cmd = "docker run --rm --memory=1gb " + \
  f"-v {PWD}/output:{OUTPUT} " + \
  f"-v {PWD}/apks:{WORKDIR}/apks " + \
  f"-t izgzhen/droid-scripts /bin/bash -c " + \
  f'"mkdir -p {PATH_LOGS}; ./dare/dare -d {DARE_RESULTS} {APK} > {PATH_LOGS}/{APKNAME}-dare.txt"'

print(cmd)
os.system(cmd)

import getpass

local_output = DARE_RESULTS.replace(WORKDIR, ".")
cmd = f"sudo chown -R {getpass.getuser()} {local_output}"
print(cmd)
os.system(cmd)