# mcp - My Colony Python

  [![DeepSource](https://deepsource.io/gh/MCW-My-Colony-Wiki/mcp.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/MCW-My-Colony-Wiki/mcp/?ref=repository-badge)
  
  [english ver readme](README.md)
  
  目前尚不支援My Colony 2

## Index of content

- [Config](##Config)
- [Classes](##Classes)
  - [FileBase](###FileBase)
  - [CategoryBase](###CategoryBase)
    - [DictCategory](####DictCategory)
    - [ListCategory](####ListCategory)
  - [UnitBase](###UnitBase)
    - [DictUnit](####DictUnit)
    - [ListUnit](####ListUnit)
  - [Base](###Base)
    - [DictBase](####DictBase)
    - [ListBase](####ListBase)

## Config

- 說明: 此模塊使用內置庫中的`configparser`提供config功能
- 路徑: `mcp.config.config`
- Sections
  - `network`
    - Options
      - `timeout: int = 3`: timeout of all the network related function

## Classes

### FileBase

- 說明: 基本與`dict`物件相同
- 路徑: `mcp.filebase.FileBase`
- 屬性
  - `name`: file的名稱
  - `dict`: file的資料
- 方法
  - `categories`: `file.keys()`的別名

### CategoryBase

- 路徑: `mcp.categorybase.CategoryBase`
- 通用屬性
  - `file`: category所屬的FileBase子類的實例
  - `name`: category的名稱
  - `data`: category的資料
- 通用方法
  - `units`: 由其子類實現

#### DictCategory

- 說明: 基本與`dict`物件相同
- 路徑: `mcp.category.DictCategory`
- 屬性
  - `dict`: `self.data`的別名
- 方法
  - `units`: `self.keys`的別名

#### ListCategory

- 說明: 基本與`list`物件相同
- 路徑: `mcp.category.ListCategory`
- 屬性
  - `list`: `self.data`的別名
- 方法
  - `units`: 與`self.__iter__`相似，但返回的是`str`物件

### UnitBase

- 路徑: `mcp.unitbase.UnitBase`
- Common 屬性
  - `file`: unit所屬的FileBase子類的實例，與`category.file`相同
  - `category`: unit所屬的CategoryBase子類的實例
  - `data`: unit的資料

#### DictUnit

- 說明: 基本與`dict`物件相同
- 路徑: `mcp.unit.DictUnit`

#### ListUnit

- 說明n: 基本與`list`物件相同
- 路徑: `mcp.unit.ListUnit`

### Base

#### CommonBase

- 說明: provide generic 方法
- 路徑: `mcp.base.CommonBase`
- 方法
  - `__delattr__`: 禁用`del object.attr`
  - `__str__`: 返回`self.name`

#### DictBase

- 說明: 提供`dict`物件的方法
- 路徑: `mcp.base.DictBase`

#### ListBase

- 說明: 提供`list`物件的方法
- 路徑: `mcp.base.ListBase`
