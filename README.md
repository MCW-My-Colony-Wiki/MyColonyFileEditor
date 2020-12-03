# mcp - My Colony Python
主要功能是整理My Colony的遊戲資料，並提供使用
目前尚不支援My Colony 2

使用方式：

## 初次使用與config()
### 1.使用package

package預設會執行check_update並有提示訊息
```py
import mcp
#mcp check_update process
#        Checking update...
#        Local game files have been updated to latest version(v1.10.0)
```

可使用config功能關閉check_update機制
(若原設定值與新設定值相同，則不會有任何變動)
```py
import mcp

mcp.config(check_update = False) #將check_update功能關閉
#Success update config file
#        "check_update": True >>> False
```


### 2.不帶參數的config()
不帶參數的config()會返回設定列表與其目前的設定值

***不會自動print!***
```py
import mcp

print(mcp.config())
#{
#        "check_update": true,
#        "show_update_message": true,
#        "timeout": 1
#}
```
*config檔使用json格式


### 3.一次調整多項設定
config()支援一次調整多項設定
```py
import mcp

mcp.config(check_update = False, show_update_message = False, timeout = 1)
#Success update config file
#        "check_update": True >>> False
```
