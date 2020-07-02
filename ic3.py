#!/usr/bin/env python3

import sys
import os
import glob

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

APK = os.path.realpath(sys.argv[1])
APK_NAME = os.path.basename(APK).replace(".apk", "")
SHA256SUM = sys.argv[2]
PKG_NAME = sys.argv[3]
INPUT_CLASSES = os.path.realpath(sys.argv[4])
PROTOBUF_OUT = sys.argv[5]

ANDROID_SDK = os.getenv("ANDROID_SDK")
ANDROID_JAR = ANDROID_SDK + "/platforms/android-23/android.jar"

OUTPUT = SCRIPT_DIR + "/output"
IC3_OUTPUT_DIR = OUTPUT + "/ic3/" + SHA256SUM

def run_cmd(cmd):
    print(cmd)
    assert os.system(cmd) == 0

OUTPUT_PATTERN = IC3_OUTPUT_DIR + "/*.txt"

if len(glob.glob(OUTPUT_PATTERN)) == 0:
    os.chdir(SCRIPT_DIR)
    run_cmd(f"mkdir -p {IC3_OUTPUT_DIR}")
    run_cmd(f"java -Xmx4g -jar {SCRIPT_DIR}/ic3-0.2.0/ic3-0.2.0-full.jar " +
        f"-input {INPUT_CLASSES} -threadcount 4 " +
        f"-apkormanifest {APK} -cp {ANDROID_JAR} -protobuf {IC3_OUTPUT_DIR}")

IC3_OUTPUT = glob.glob(OUTPUT_PATTERN)
assert len(IC3_OUTPUT) == 1
IC3_OUTPUT = IC3_OUTPUT[0]
os.system("cp " + IC3_OUTPUT + " " + PROTOBUF_OUT)