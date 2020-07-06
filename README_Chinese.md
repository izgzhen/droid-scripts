Droid Scripts
=====

对第三方工具 Jar 包的脚本拓展，或者对 Android SDK 工具的拓展比如 `adb` (在 `path/to/sdk/platform-tools` 里), `aapt` (在 `path/to/sdk/build-tools/<version>` 里面).

注：安装 build tools `path/to/sdk/tools/bin/sdkmanager 'build-tools;29.0.3'`


## Launch app on connected device 启动设备上的应用

依赖 python3 和 `msbase` 包.


```
./launch-apk.py launch path/to/apk
```

注: 如何打出 application label （应用名）and package （包名）：

```
./launch-apk.py label path/to/apk
./launch-apk.py package path/to/apk
```


## Make an APK debuggable 修改 APK 为可调试状态
- `python debug-sign.py <input-apk-path> <output-apk-path>`

## Decompile APK to Smali code 反汇编到 Smali 代码

```
baksmali d path/to/apk -o path/to/output/dir
```

Version: 2.4.0, from https://github.com/JesusFreke/smali/

smali 的用法类似 


## Decompile APK to Smali and other resources 反汇编到 Smali 代码和资源文件

```
apktool d path/to/apk -o path/to/output/dir
```

Version: 2.4.1, from https://ibotpeaches.github.io/Apktool/

## Dump classes list 把 class 列表打到文件里

```
pkg-classes path/to/apk path/to/txt
```

## Check the view hierarchy of APK dynamically 动态查看GUI结构

1. 先用 `debug-sign.apk` 做一个可调试的版本 
2. (选项 1) 用 Android Studio，选 debug/profile
  - Tools（工具） -> Layout Inspector（布局查看器）
    + 选对应 Activity
3. (选项 2) 用脚本工具:
  - `./adb-uidump path/to/output/xml`
  - `./adb-uidump-compressed path/to/output/xml`

## Dump metadata about APK 把元信息打出来

- `aapt dump badging path/to/apk`
  - `application-label:`: 打出来应用名
  - `package: name`: 打出来包名
- `aapt dump permissions path/to/apk`: 打出来权限信息

## Copy back APK installed on phone 把手机上的 APK 拷下来

```bash
adb shell pm list packages # find the package name from the output
adb shell pm path <package-name> # outputs <target-apk-path>
adb pull <target-apk-path> <apk-output>
```

## Install APK to phone via CLI 从命令行安装 APK 到手机上

```
adb install path/to/apk
```

## Retargeting Dex to Java Classes 把 Dex 转换成 Java 类文件

注: 先构建 Docker 镜像：执行 `make` 
保证 APK 的源文件 (not symbolic link) 在 `apks/` 文件夹里面.

```
./dare.py apks/example.apk <sha256sum>
```

输出在 `output/dare/`

## Inter-Component Communication (ICC) analysis ICC 分析

注: 依赖上面的 "Dare" 工具. 主要要设置 `ANDROID_SDK` 环境变量到
Android SDK 文件夹，这样才能找到 `$ANDROID_SDK/platforms/android-23/android.jar`.


```
path/to/ic3.py path/to/example.apk <sha256sum> <apk-package-name> path/to/dare/classes path/to/output.txt
```

输出在 `path/to/output.txt`

## 打出设备上正在运行的 Activity


```
adb shell dumpsys activity
```

## 相关资源

- https://github.com/strazzere/android-scripts
- adbshell.com
- [Reverse engineering and penetration testing on Android apps: my own list of tools](https://www.andreafortuna.org/2019/07/18/reverse-engineering-and-penetration-testing-on-android-apps-my-own-list-of-tools/)
