#!/usr/bin/env python3

import sys
import os

APK = sys.argv[1]
APK_NAME = os.path.basename(APK).replace(".apk", "")
SHA256SUM = sys.argv[2]
PKG_NAME = sys.argv[3]
PROTOBUF_OUT = sys.argv[4]

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

ANDROID_SDK = os.getenv("ANDROID_SDK")
ANDROID_JAR = ANDROID_SDK + "/platforms/android-23/android.jar"

OUTPUT = SCRIPT_DIR + "/output"
IC3_OUTPUT_DIR = OUTPUT + "/ic3/" + SHA256SUM
IC3_OUTPUT = IC3_OUTPUT_DIR + "/" + PKG_NAME + "_5.txt" # 5 is the version

def run_cmd(cmd):
    print(cmd)
    os.system(cmd)

if os.path.exists(IC3_OUTPUT):
    os.system("cp " + IC3_OUTPUT + " " + PROTOBUF_OUT)
    exit(0)

os.chdir(SCRIPT_DIR)
run_cmd(f"./dare.py {APK} {SHA256SUM}")
run_cmd(f"mkdir -p {IC3_OUTPUT_DIR}")
run_cmd(f"java -jar {SCRIPT_DIR}/ic3-0.2.0/ic3-0.2.0-full.jar " +
    f"-input {OUTPUT}/dare/{SHA256SUM}/retargeted/{APK_NAME}/ " +
    f"-apkormanifest {APK} -cp {ANDROID_JAR} -protobuf {IC3_OUTPUT_DIR}")

os.system("cp " + IC3_OUTPUT + " " + PROTOBUF_OUT)