# mcfp - My Colony File Parser

  [![DeepSource](https://deepsource.io/gh/MCW-My-Colony-Wiki/MyColonyFileParser.svg/?label=active+issues&show_trend=true&token=zjOyAP4RLEuWcm5YOU1NQJW_)](https://deepsource.io/gh/MCW-My-Colony-Wiki/MyColonyFileParser/?ref=repository-badge)
  
  [english ver readme](README.md)
  
  目前尚不支援My Colony 2

## Index of content

- [Config](#config)
- [Classes](#classes)
  - [Base](#base)
    - [CommonBase](#commonbase)
    - [DictBase](#dictbase)
    - [ListBase](#listbase)
  - [FileBase](#filebase)
    - [Game](#game)
    - [Strings](#strings)
  - [CategoryBase](#categorybase)
    - [DictCategory](#dictcategory)
    - [ListCategory](#listcategory)
  - [UnitBase](#unitbase)
    - [DictUnit](#dictunit)
    - [ListUnit](#listunit)
- [Exceptions](#exceptions)
  - [MCFPerror](#mcfperror)
    - [FileError](#fileerror)
      - [InvalidFileChannel](#invalidfilechannel)
      - [InvalidFileVersion](#invalidfileversion)
      - [InvalidFileName](#invalidfilename)
    - [CategoryError](#categoryerror)
      - [InvalidCategoryName](#invalidcategoryname)
    - [UnitError](#uniterror)
      - [InvalidUnitName](#invalidunitname)

## Config

- 說明: 此模塊使用內置庫中的`configparser`提供config功能
- 路徑: `mcp.config.config`
- Sections
  - `network`
    - Options
      - `timeout: int = 3`: timeout of all the network related function

## Classes

### Base

#### CommonBase

- 說明: 提供通用方法
- 路徑: `mcfp.base.CommonBase`
- 方法
  - `__delattr__`: 禁用`del object.attr`
  - `__str__`: 返回`self.name`

#### DictBase

- 說明: 提供`dict`物件的方法
- 路徑: `mcfp.base.DictBase`
- 繼承: [CommonBase](#commonbase)

#### ListBase

- 說明: 提供`list`物件的方法
- 路徑: `mcfp.base.ListBase`
- 繼承: [CommonBase](#commonbase)

### FileBase

- 說明: 基本與`dict`物件相同
- 路徑: `mcfp.filebase.FileBase`
- 繼承: [DictBase](#dictbase)
- 屬性
  - `name`: file的名稱
  - `dict`: file的資料
- 方法
  - `categories`: `file.keys()`的別名

#### Game

- 說明: 代表像[game.js](https://www.apewebapps.com/apps/my-colony/1.14.0/game.js)這樣的檔案
- 路徑: `mcfp.file.Game`
- 繼承: [FileBase](#filebase)

#### Strings

- 說明: 代表像[strings.js](https://www.apewebapps.com/apps/my-colony/1.14.0/strings.js)這樣的檔案
- 路徑: `mcfp.file.Strings`
- 繼承: [FileBase](#filebase)

### CategoryBase

- 路徑: `mcfp.categorybase.CategoryBase`
- 通用屬性
  - `file`: category所屬的FileBase子類的實例
  - `name`: category的名稱
  - `data`: category的資料
- 通用方法
  - `units`: 由其子類實現

#### DictCategory

- 說明: 基本與`dict`物件相同
- 路徑: `mcfp.category.DictCategory`
- 繼承: [DictBase](#dictbase), [CategoryBase](#categorybase)
- 屬性
  - `dict`: `self.data`的別名
- 方法
  - `units`: `self.keys`的別名

#### ListCategory

- 說明: 基本與`list`物件相同
- 路徑: `mcfp.category.ListCategory`
- 繼承: [ListBase](#listbase), [CategoryBase](#categorybase)
- 屬性
  - `list`: `self.data`的別名
- 方法
  - `units`: 與`self.__iter__`相似，但返回的是`str`物件

### UnitBase

- 路徑: `mcfp.unitbase.UnitBase`
- Common 屬性
  - `file`: unit所屬的FileBase子類的實例，與`category.file`相同
  - `category`: unit所屬的CategoryBase子類的實例
  - `data`: unit的資料

#### DictUnit

- 說明: 基本與`dict`物件相同
- 路徑: `mcfp.unit.DictUnit`
- 繼承: [DictBase](#dictbase), [UnitBase](#unitbase)

#### ListUnit

- 說明: 基本與`list`物件相同
- 路徑: `mcfp.unit.ListUnit`
- 繼承: [ListBase](#listbase), [UnitBase](#unitbase)

## Exceptions

### MCFPError

MCFP的異常基類

- 繼承: [Exception](https://docs.python.org/zh-cn/3/library/exceptions.html#Exception)

### FileError

File相關異常

- 繼承: [MCFPerror](#mcfperror)

### InvalidFileChannel

File channel無效

- 繼承: [FileError](#fileerror)

### InvalidFileVersion

File version無效

- 繼承: [FileError](#fileerror)

### InvalidFileName

File name無效

- 繼承: [FileError](#fileerror)

### CategoryError

Category相關異常

- 繼承: [MCFPError](#mcfperror)

### InvalidCategoryName

Category name無效

- 繼承: [CategoryError](#categoryerror)

### UnitError

Unit相關異常

- 繼承: [MCFPError](#mcfperror)

### InvalidUnitName

Unit name無效

- 繼承: [UnitError](#uniterror)
