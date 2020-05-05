#!/usr/bin/env python3

import sys
import os

APK = sys.argv[1]
APKNAME = os.path.basename(APK)
APKNAME_NO_SUFFIX = APKNAME.replace(".apk", "")
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
assert os.getcwd() == SCRIPT_DIR
ANDROID_SDK = os.getenv("ANDROID_SDK")
ANDROID_JAR = ANDROID_SDK + "/platforms/android-23/android.jar"

OUTPUT = SCRIPT_DIR + "/output"
IC3_OUTPUT = OUTPUT + "/ic3"

def run_cmd(cmd):
    print(cmd)
    os.system(cmd)

run_cmd(f"mkdir -p {IC3_OUTPUT}/{APKNAME}")
run_cmd(f"java -jar {SCRIPT_DIR}/ic3-0.2.0/ic3-0.2.0-full.jar " +
    f"-input {OUTPUT}/dare/results/retargeted/{APKNAME_NO_SUFFIX}/ " +
    f"-apkormanifest {APK} -cp {ANDROID_JAR} -protobuf {IC3_OUTPUT}/{APKNAME}")