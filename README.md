Droid Scripts
=====

Executable scripts for helping with Android related work.

Most of them are either wrappers of existing third-party tool's released jars or
Android SDK tools' executables e.g. `adb` (inside `path/to/sdk/platform-tools`),
`aapt` (inside `path/to/sdk/build-tools/<version>`).

NOTE: Install build tools
`path/to/sdk/tools/bin/sdkmanager 'build-tools;29.0.3'`

## Launch app on connected device

Depends on python3 and `msbase` package.

```
./launch-apk.py launch path/to/apk
```

NOTE: this python script also supports printing the application label
and package of an apk:

```
./launch-apk.py label path/to/apk
./launch-apk.py package path/to/apk
```


## Make an APK debuggable
- `python debug-sign.py <input-apk-path> <output-apk-path>`

## Decompile APK to Smali code

```
baksmali d path/to/apk -o path/to/output/dir
```

Version: 2.4.0, from https://github.com/JesusFreke/smali/ (also include `smali`)

## Decompile APK to Smali and other resources

```
apktool d path/to/apk -o path/to/output/dir
```

Version: 2.4.1, from https://ibotpeaches.github.io/Apktool/

## Dump classes list

```
pkg-classes path/to/apk path/to/txt
```

## Check the view hierarchy of APK dynamically

1. Make a debuggable copy of it using `debug-sign.apk`
2. (Option 1) Use Android Studio to debug/profile it
  - Tools -> Layout Inspector
      + Choose the corresponding Activity
3. (Option 2) Use scripts:
  -  `adb-uidump path/to/output/xml`
  -  `adb-uidump-compressed path/to/output/xml`

## Dump metadata about APK

- `aapt dump badging path/to/apk`
  - `application-label:`: show package label
  - `package: name`: show package name
- `aapt dump permissions path/to/apk`: show permission

## Copy back APK installed on phone

```bash
adb shell pm list packages # find the package name from the output
adb shell pm path <package-name> # outputs <target-apk-path>
adb pull <target-apk-path> <apk-output>
```

## Install APK to phone via CLI

```
adb install path/to/apk
```

## Retargeting Dex to Java Classes

NOTE: Build the Docker image with `make` first

Make sure your APK file (not symbolic link) is under `apks` in this directory.

```
./dare.py apks/example.apk <sha256sum>
```

Then you can find (Java classes) outputs in `output/dare/`

## Inter-Component Communication (ICC) analysis

NOTE: this depends on "Dare" introduced above.
Also, you should set env var `ANDROID_SDK` to the Android SDK directory, such that
the tool can find `$ANDROID_SDK/platforms/android-23/android.jar`.

```
path/to/ic3.py path/to/example.apk <sha256sum> <apk-package-name> path/to/dare/classes path/to/output.txt
```

Then you can find (text-format Protobuf) output at `path/to/output.txt`

## Getting name of current activity

```
adb shell dumpsys activity
```

## Related work

- https://github.com/strazzere/android-scripts
- adbshell.com
- [Reverse engineering and penetration testing on Android apps: my own list of tools](https://www.andreafortuna.org/2019/07/18/reverse-engineering-and-penetration-testing-on-android-apps-my-own-list-of-tools/)
