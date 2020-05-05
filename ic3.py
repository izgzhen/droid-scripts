#!/usr/bin/env python3

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

APK = os.path.realpath(sys.argv[1])

os.system("cp " + APK + " " + SCRIPT_DIR + "/apks")
APK = SCRIPT_DIR + "/apks/" + os.path.basename(APK)

APK_NAME = os.path.basename(APK).replace(".apk", "")
SHA256SUM = sys.argv[2]
PKG_NAME = sys.argv[3]
PROTOBUF_OUT = sys.argv[4]

ANDROID_SDK = os.getenv("ANDROID_SDK")
ANDROID_JAR = ANDROID_SDK + "/platforms/android-23/android.jar"

OUTPUT = SCRIPT_DIR + "/output"
IC3_OUTPUT_DIR = OUTPUT + "/ic3/" + SHA256SUM
IC3_OUTPUT = IC3_OUTPUT_DIR + "/" + PKG_NAME + "_5.txt" # 5 is the version

def run_cmd(cmd):
    print(cmd)
    assert os.system(cmd) == 0

if os.path.exists(IC3_OUTPUT):
    print("Exists " + IC3_OUTPUT)
    os.system("cp " + IC3_OUTPUT + " " + PROTOBUF_OUT)
    exit(0)

os.chdir(SCRIPT_DIR)
INPUT_CLASSES = f"{OUTPUT}/dare/{SHA256SUM}/retargeted/{APK_NAME}/"

if not os.path.isdir(INPUT_CLASSES):
    run_cmd(f"./dare.py {APK} {SHA256SUM}")
run_cmd(f"mkdir -p {IC3_OUTPUT_DIR}")
run_cmd(f"java -jar {SCRIPT_DIR}/ic3-0.2.0/ic3-0.2.0-full.jar " +
    f"-input {INPUT_CLASSES} " +
    f"-apkormanifest {APK} -cp {ANDROID_JAR} -protobuf {IC3_OUTPUT_DIR}")

os.system("cp " + IC3_OUTPUT + " " + PROTOBUF_OUT)