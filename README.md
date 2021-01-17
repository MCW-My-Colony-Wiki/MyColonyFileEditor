[![DeepSource](https://deepsource.io/gh/Euxcbsks/mcp.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/Euxcbsks/mcp/?ref=repository-badge)

# mcp - My Colony Python
整理My Colony的遊戲資料，並提供方便獲取資料的功能
**目前尚不支援 My Colony 2**

# To do
1. - [x] 下載遊戲資料時，立即對其進行format處理並儲存，以提高後續載入速度
2. - [x] 修復當一個@run_here function在另一個@run_here function內使用時，導致的工作路徑錯誤
3. - [x] 完成operate.developer中的檔案列表產生器及其應用
4. 待定

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
	"check_update": true,
	"auto_update": true,
	"timeout": 1
}
```
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
獲取遊戲資料的功能

### getsource
#### Parameters
* source(str): 想取得的Source object名稱
  * 目前選項僅有'game'和'strings'兩種

#### Return
返回一個Source object

#### Error
* TypeError: 參數型別不正確，詳細信息請查看報錯
* InvalidSourceError: 無效的source名稱

#### Usage
```py
source = getsource('game')

print(source.name)
```
Output:
```
game
```

### getcat
#### Parameters
* source(str, Source): 想取得Category object的source名稱或Source object
* category(str): 想取得的Category object名稱
  * 有效的category可透過Source.categories取得

#### Return
返回一個Category object

#### Error
* TypeError: 參數型別不正確，詳細信息請查看報錯
* InvalidSourceError: 無效的source名稱
* InvalidCategoryError: 無效的category名稱

#### Usage
```py
cat = getcat('game 'meta')

print(cat.name)
```
or
```py
source = getsource('game')
cat = getcat(source, 'meta')

print(cat.name)
```
Output:
```
meta
```

### getunit
#### Parameters
* category(Category): 想取得Unit object的Category object
* unit(str): 想取得的Unit object名稱

or

* source(str, Source): 想取得Unit object的Category object所屬的source名稱或Source object
* category(str, Category): 想取得Unit object的category名稱或Category object
* unit(str): 想取得的Unit object名稱

函式會透過Parameters的數量自動判斷使用何種運作方式

當Parameters的數量為2時，第一個參數必須為Category object

由於存在Category object的資料，其型態可能為list, dict或ListUnit(list of unit)

故在取用資料時務必小心確認Category object的資料型態

#### Return
返回一個繼承自Unit的object

#### Error
* TypeError: 參數型別不正確，詳細信息請查看報錯
* InvalidSourceError: 無效的source名稱
* InvalidCategoryError: 無效的category名稱
* InvalidUnitError: 無效的unit名稱

#### Usage
```py
cat = getcat('game 'meta')

print(type(cat.data))

unit = getunit(cat, 'buildVersion')

print(unit)
```
Output:
```
1.11.0
```

or

```py
unit = getunit('game 'buildings 'Lander')

print(unit)
```
Output:
```
Lander
```

## class
package中定義的class

主要使用的類:
* Source
* Category
* Unit

為了提供附加功能而產生的類
* ListUnit
* 所有繼承自Unit的類

### Source
#### Attributes
* name: Source的名字
* data: dict型別的Source資料
* categories: 此Source所有的category

#### Usage
##### print
顯示Source object的名字

```py
source = getsource('game')

print(source)
```

Output:
```
game
```

##### len
傳回此Source object有多少Category

```py
source = getsource('strings')

print(len(source))
```

Output:
```
4
```

##### loop
每次傳回一個Category object

Category object是在需要時才建立的

```py
source = getsource('game')

for cat in source:
    print(cat)
```

##### in
檢查物件是否在此Source object裡

支援Category object和str兩種型態

```py
source = getsource('game')
cat = getcat(source, 'meta')

print('meta' in source)
print(cat in source)
```

Output:
```
True
True
```

### Category
#### Attributes
共通Attributes:
* name: Category的名字
* source: Category所屬的Source
* data: dict, list or ListUnit型別的Category資料

當type(cat.data) == ListUnit才會有的Attributes
* units: Category的Unit列表

當type(cat.data) == dict才會有的Attributes
* keys: Category的key列表

#### Usage
##### print
當遇到不同型別的cat.data時，會使用不同的顯示方式

設計時比照列表或字典的呈現方式，顯示其所持的資料

```py
cat = getcat('game category_name)

print(cat)
```

Output:
* hasattr(cat, units)
  * print(cat.units)
* hasattr(cat, keys)
  * print(cat.keys)
* else
  * print(cat.data)

##### len
* if type(cat.data) == ListUnit
  * 傳回此Category有多少Unit
* if type(cat.data) == dict
  * 傳回此Category有多少key
* if type(cat.data) == list
  * 傳回此Category有多少物件

```py
cat = getcat('game 'buildings)

print(len(cat))
```

Output:
```
561
```

##### loop
* if type(cat.data) == dict:
  * 傳回key
* if type(cat.data) == list or ListUnit:
  * 傳回物件或Unit

```py
cat = getcat('game 'meta')

for item in cat:
	print(item)
```

Output:
```
name
titletheme
theme
...
...
...
```

##### in
檢查物件是否在此Category內

支援Unit object和str兩種型態

Unit object僅在type(cat.data) == ListUnit的Category才有可能傳回True

```py
cat = getcat('game 'buildings')
unit = getunit(cat, 'Lander')

print('Lander' in cat)
print(unit in cat)
```

Output:
```
True
True
```

### Unit
#### Attributes
共通Attributes
* data: dict型別的Unit資料
* source: Unit所在的Source
* category: Unit所在的Category

繼承自Unit的class，會各自設定特有的attributes

#### Usage
##### print
顯示Unit的name或title

```py
unit = getunit('game 'buildings 'Lander')

print(unit)
```

Output:
```
Lander
```

### Inherited from Unit
#### VideoTutorial
##### Attributes
* rtitle: format前的title
* title: format後的title
* rauthor: format前的author name
* author: format後的author name
* url: YouTube上的11碼影片url

#### Soundtrack
##### Attributes
* title: title
* file_format: 檔案格式
* seconds: 音檔時長

#### Map
##### Attributes
* buildings: 開始新遊戲時，預先建造好的建築
* color: 地圖的色彩特效
* color_strength: 色彩特效強度
* desc: 顯示在選單的地圖資訊
* difficulty: 生存難度
* disasters: 此地圖可能發生的災難
* ground: 地面使用的圖片
* icon: 選單上的地圖圖標
* mapach: 未知
* name: 地圖名稱
* ocean: 海洋使用的圖片
* region: 區域使用的地面
* resources: 天然資源種類
* river: 河流使用何種資源
* river_color: 河流的顏色
* river_position: 合流的位置
* rname: format前的name
* shore_connectors: 未知
* shores: 未知
* techs: 地圖提供的初始科技
* terrains: 地圖自帶的環境特色
* weather: 可能出現的天氣
* welcome: 初次進入地圖時發送的訊息

#### Race
##### Attributes
* color: 未知
* default: 一般人民使用的圖標
* desc: 顯示於選單的種族資訊
* name: 種族名稱
* narcotics: 未知
* retired: 退休人民使用的圖標
* student: 學生使用的圖標
* techs: 種族提供的初始科技
* tourist: 遊客使用的圖標

#### Civilization
##### Attributes
* backstory: 文明的背景故事
* building: 文明預先建造好的建築
* colonists: 文明初始的殖民者數量
* desc: 顯示在選單的文明資訊
* icon: 顯示在選單的文明圖標
* maps: 此文明可選的地圖類型
* name: 文明名稱
* race: 此文明可選的種族類型
* resources: 文明的初始可用資源
* rname: format前的name
* server: 未知
* techs: 文明提供的初始科技
* vehicles: 文明的初始可用車輛
* welcome: 初次進入地圖時發送的訊息

#### Tile
##### Attributes
* flip: 是否可以翻轉
* image: 使用的圖片
* name: 圖標的名稱
* width: 圖標的寬度

#### Resource
##### Attributes
* amount: 未知
* color: 當顯示資源獲取時，此資源的字體顏色
* essential: 此資源是否會隨時間自然減少
* gift: 此資源是否可以轉送
* icon: 此資源的圖標
* indicator: 此資源的縮寫
* max: 可持有的最大值
* name: format後的name
* price: 未知，推測是在市場上的基礎價格
* rname: format前的name
* starting: 新地圖預設擁有此數量的此資源
* toxic: 此資源的成癮程度

#### Utility
##### Attributes
* color: 此資源的字體顏色
* essential: 此資源是否會隨時間自然減少
* icon: 此資源的圖標
* indicator: 此資源的縮寫
* name: 此資源的名稱

#### Occupation
##### Attributes
* indicator: 職業的圖標
* name: format後的職業名稱
* rname: format前的職業名稱
* salary: 此職業的預設基本薪資
* tiles: 為此職業的人民，其所使用的圖標

#### Terrain
##### Attributes
* additional_connectors: 未知
* capacity: 此自然資源的資源容量
* decay_rate: 此自然資源的轉化速度
* decays_to: 可轉換為的自然資源
* destruction_collect: 破壞此自然資源時可獲得的資源
* generate_amount: 暫無用
* generate_time: 暫無用
* generates: 暫無用
* height: 圖標高度
* icon: 此自然資源在選單中的圖標
* indestructable: 
* light_effects: 此自然資源的色彩特效
* name: format後的自然資源名稱
* passable: 車輛是否可以越過此自然資源
* provides: 能產生的資源
* raid_items: 未知
* rname: format前的自然資源名稱
* shore: 未知
* spread_rate: 此自然資源的擴散速度
* spread_resource: 擴散出的資源
* tile: 此自然資源在地圖上的圖標
* width: 圖標寬度

#### Technology
##### Attributes
* cost: 解鎖此科技所需的資源
* desc: 此科技的資訊
* icon: 此科技的圖標
* independence: 解鎖此科技是否需要殖民地獨立
* name: format後的科技名稱
* premium: 解鎖此科技是否需要解鎖高級版遊戲
* rname: format前的科技名稱
* stage: 解鎖此科技所需的stage
* techs: 此科技的前置科技

#### Building
##### Attributes
* becomes_terrain: 此建築是否會成為自然資源
* can_build_over: 此建築可蓋過的物件
* can_export: 此建築可出口的資源
* can_import: 此建築可進口的資源
* capitol: 此建築是否為Capital
* categories: 此建築在遊戲內所屬的分類列表
* chain: 未知
* chop_shop: 此建築是否為Chop Shop
* col_gen_rate: 此建築產生殖民者的速度
* comms_hub_bldg: 此建築是否為Comms Hub Bldg
* connects_to: 未知
* consulate: 此建築是否為Consulate
* cost: 建造此建築所需的資源
* creates_dec_units: 未知
* default_house_cost: 未知
* desc: 此建築的資訊
* educates: 此建築可容納的學生數
* embargo_immune: 未知
* embassy: 此建築是否為Embassy
* entertainmentCost: 此建築消耗的娛樂設施數量
* entertains: 未知
* first_build_mes: 初次建造此建築時顯示的訊息
* flip: 此建築是否可以翻轉
* fuel: 未知
* generate_amount: 每生產一次資源可獲得的數量
* generate_time: 每生產一次資源所需的週期時間
* generates: 此建築可以生產的資源
* gift_capacity: 作為禮物贈送時，此資源的容量
* heals: 此建築可容納多少病人
* height: 圖標高度
* independence: 建造此建築是否需要殖民地獨立
* indicator: 此建築的圖標
* jail_capacity: 此建築可容納多少犯人
* light_effects: 此建築的色彩特效
* limit: 建造數量限制
* name: format後的name
* occupation: 於此建築工作的人民職業
* online_trade_depot: 未知
* packs_to: 可變化為
* passable: 是否可被越過
* premium: 是否需要解鎖高級版遊戲
* produces: 可以在此建造的車輛
* providesIQ: 可將人民的IQ提升至此數值
* provides_utility: 可產生的Utilities
* refines: 此建築可轉化的資源
* regional_port: 未知
* render_static: 是否可降低渲染資源消耗
* requiresIQ: 於此建築工作所需的IQ
* requires_utility: 運行此建築所需的Utilities
* requires_workers: 運行此建築所需的Workers
* rname: format前的name
* sell: 賣掉這個建築時可獲得的資源
* sell_warning: 賣掉這個建築時所顯示的警告
* shelter: 此建築提供的房間數
* sign: 此建築是否為Sign
* smelts: 消耗資源並產生另一種資源
* sound: 選中此建築時撥放的聲音
* speed: 車輛在此建築上移動時提供的速度加成
* stage: 建造此建築所需的Stage
* stargate: 此建築是否為Stargate
* stores: 此建築可容納的資源
* subterranean_tile: 未知
* tax: 每一個建築需繳納的稅額
* tech: 建造此建築所需的科技
* tile: 建築的圖標
* tourist_doorway: 是否為遊客進出的管道
* tourists: 建築可容納的遊客數量
* trade_capacity: 建築提供的交易容量
* transModeColor: 未知
* transit_capacity: 未知
* transit_path: 未知
* transit_unit: 未知
* unlocks_achievement: 建造此建築可獲得的成就
* unlocks_gov: 建造此建築可解鎖的Government level
* upgrade: 可升級至的建築
* upkeep_cost: 未知
* width: 圖標寬度
* workers: 可容納的最大員工數

#### Vehicle
##### Attributes
* attack_confirm_sound: 確認攻擊時撥放的音效
* build_categories: 車輛所屬的分類
* build_confirm_sound: 確認建造時撥放的音效
* canRaid: 未知
* capacity: 車輛可容納的資源數量
* colonist_carry_capacity: 車輛可容納的殖民者數量
* cost: 建造此車輛所需的資源
* creation_sound: 建造時撥放的音效
* deploy_confirm_sound: 確認放置時撥放的音效
* deploys_to: 放置後變為的建築
* desc: 車輛的資訊
* first_build_mes: 初次建造此車輛時顯示的訊息
* fly: 此車輛是否可飛行
* harvest_confirm_sound: 確認開始收集資源時撥放的音效
* harvests: 車輛可收集的資源
* independence: 建造此車輛是否需要殖民地獨立
* indicator: 車輛的圖標
* move_confirm_sound: 確認移動時撥放的音效
* name: format後的name
* premium: 建造此車輛是否需要解鎖高級版遊戲
* produces: 未知
* rname: format前的name
* selection_sound: 選中此車輛時撥放的聲音
* sell: 賣掉車輛後可獲得的資源
* sell_warning: 賣掉車輛時顯示的警告
* speed: 車輛的基礎速度
* stage: 建造此車輛所需的Stage
* tech: 建造此車輛所需的科技
* tile: 車輛的圖標
* vehicle_carry_capacity: 每次收集資源可容納的最大資源量
