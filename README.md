# mcp - My Colony Python

  [![DeepSource](https://deepsource.io/gh/MCW-My-Colony-Wiki/mcp.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/MCW-My-Colony-Wiki/mcp/?ref=repository-badge)
  
  [中文版readme](README_zh.md)
  
  current not suppot My Colony 2

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

- Description: this module use `configparser` that in stdlib to provide config function
- Path: `mcp.config.config`
- Sections
  - `network`
    - Options
      - `timeout: int = 3`: timeout of all the network related function

## Classes

### FileBase

- Description: basically same as `dict` object
- Path: `mcp.filebase.FileBase`
- Attributes
  - `name`: file name
  - `dict`: file data
- Method
  - `categories`: alias of `file.keys()`

### CategoryBase

- Path: `mcp.categorybase.CategoryBase`
- Common attributes
  - `file`: instance of subclass of FileBase which this category belong
  - `name`: category name
  - `data`: category data
- Common method
  - `units`: Implemented by subclass

#### DictCategory

- Description: basically same as `dict` object
- Path: `mcp.category.DictCategory`
- Attributes
  - `dict`: alias of `self.data`
- Method
  - `units`: alias of `self.keys`

#### ListCategory

- Description: basically same as `list` object
- Path: `mcp.category.ListCategory`
- Attributes
  - `list`: alias of `self.data`
- Method
  - `units`: similar with `self.__iter__` but return str object

### UnitBase

- Path: `mcp.unitbase.UnitBase`
- Common attributes
  - `file`: instance of subclass of FileBase which this unit belong, same as `category.file`
  - `category`: instance of subclass of CategoryBase which this unit belong
  - `data`: unit data

#### DictUnit

- Description: basically same as `dict` object
- Path: `mcp.unit.DictUnit`

#### ListUnit

- Descriptionn: basically same as `list` object
- Path: `mcp.unit.ListUnit`

### Base

#### CommonBase

- Description: provide generic method
- Path: `mcp.base.CommonBase`
- Method
  - `__delattr__`: disable `del object.attr`
  - `__str__`: return `self.name`

#### DictBase

- Description: provide method of `dict` object
- Path: `mcp.base.DictBase`

#### ListBase

- Description: provide method of `list` object
- Path: `mcp.base.ListBase`
