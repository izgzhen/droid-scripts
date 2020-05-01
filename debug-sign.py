import os
import sys
import tempfile

def run(cmd):
    print(cmd)
    assert os.system(cmd) == 0

APK = sys.argv[1]
OUT_APK = sys.argv[2]
temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".apk").name
tmp_dir = tempfile.TemporaryDirectory().name

# Use apktool to add the debug sign
# NOTE: use -r flag skips resource decoding, which avoids a lot of decoding
#       exceptions
run(f"./apktool d -f {APK} -o {tmp_dir}")
run(f"./apktool b -d {tmp_dir} -o {temp_file}")

# re-sign  the APK
run(f"java -jar sign.jar {temp_file}")
temp_file_signed = temp_file.replace(".apk", ".s.apk")
run(f"cp {temp_file_signed} {OUT_APK}")
