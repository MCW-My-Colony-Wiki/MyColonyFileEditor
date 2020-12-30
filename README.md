# mcp - My Colony Python
整理My Colony的遊戲資料，並提供方便獲取資料的功能
**目前尚不支援My Colony 2**

## package

初次使用package時，會自動下載最新版的遊戲檔案(v1.11.0版約3MB)
```py
import mcp
```
Output:
```
Missing source file, trying to download...
Download completed
```
從開始下載到結束，整個過程大約需等待30秒至1分鐘

## config
有關設定值的操作

### config()
使用不帶參數的config()以取得目前的設定值
```py
import mcp

print(mcp.config())
```
Output:
```
{
	"self_check": true,
	"check_update": true,
	"auto_update": true,
	"timeout": 1
}
```
* self_check: 啟動時進行自我檢查
* check_update: 啟動時檢查遊戲檔案是否有更新，有的話詢問用戶是否要更新
* auto_update: 啟動時檢查遊戲檔案是否有更新，有的話自動進行更新
* timeout: 有關網路的操作，其timeout時間的設定值

### config(**paras)
config()支援一次更改多項設定
若該項目原先的設定值與你設定的值相同，則不會進行更改
並且如果有更改的話，會顯示一個更改列表
```py
import mcp

mcp.config(self_check = False, check_update = False, auto_update = False, timeout = 1)
```
Output:
```
Success update config file
	"check_update": True False
```

## operate
所有獲取遊戲資料的功能

### getunit(part, unit)