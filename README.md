Droid Scripts
=====

Executable scripts for helping with Android related work.

- `python debug-sign.py <input-apk-path> <output-apk-path>`
  - Make an APK debuggable
- `baksmali`/`smali` version: 2.4.0
  + https://github.com/JesusFreke/smali/
- `apktool` version: 2.4.1
  + https://ibotpeaches.github.io/Apktool/
- `pkg-classes path/to/apk path/to/txt`:
  + Dump classes in `apk` to `txt`

Most of them are either wrappers of existing third-party tool's released jars or
Android SDK tools' executables e.g. `adb`, `aapt`.

