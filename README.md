Chrome DevTools Python Wrapper
------------------------------

"Remote Debugging Protocol 1.1": https://developer.chrome.com/devtools/docs/protocol/1.1/index

Debug Google Chrome.app on Mac OS X
```
open /Applications/Google\ Chrome.app --args --remote-debugging-port=9222
```

Debug chrome.exe on Mac OS X (untested)
```
C:\Program Files\ (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222
```

Debug Android Webview within Emulator on Mac OS X or Linux
```
EMULATOR=emulator-5556
APP=bbc.mobile.sport.ww
PORT=`adb -s $EMULATOR shell ps | grep $APP | awk '{print $2}'`
adb -s $EMULATOR forward tcp:9222 localabstract:webview_devtools_remote_$PORT
```