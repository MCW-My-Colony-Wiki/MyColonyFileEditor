[![DeepSource](https://deepsource.io/gh/MCW-My-Colony-Wiki/mcp.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/MCW-My-Colony-Wiki/mcp/?ref=repository-badge)

[中文版](README_zh.md)

# mcp - My Colony Python
**current not suppot My Colony 2**

Index:
- [mcp - My Colony Python](#mcp---my-colony-python)
	- [Config](#config)
	- [Operate](#operate)
		- [developer](#developer)
		- [source(module)](#sourcemodule)
	- [Classes](#classes)
		- [Source](#source)
		- [Category](#category)
		- [Unit](#unit)

if you are first time `import mcp`, it will auto download latest game file and generate config file

## Config
`mcp.config()`

return all the config data

option description
* check_update: check if the game is updated
* auto_update: if there is an update, auto upgrade package
* update_from: update source, `stable` or `latest`
* timeout: timeout for all netwokrk interactions, unit is second(s)

`config(**paras)`

update config data and print changes

* if new value is equal to the old value, it will not appear in the changes

e.g.

```py
config(timeout = 2)
```
output
```
changes
    timeout 1 -> 2
```
## Operate
### developer
* del_pyc
### source(module)
* source
  * argument
    * **file**([str](https://docs.python.org/3/library/stdtypes.html#str)): there are currently `game` and `strings` two files
  * return
    * [Source](###Source) object
  * error
    * **InvalidSourceError**: file is not 'game' or 'strings'

* category
  * argument
    * **from_source**([str](https://docs.python.org/3/library/stdtypes.html#str), [Source](##Source)): if `type(from_source)` is not [Source](##Source), a Source object will auto generate
    * **name**([str](https://docs.python.org/3/library/stdtypes.html#str)): name of category
  * return
    * [Category](##Category) object
  * error
    * **InvalidSourceError**: only raise when `type(from_source)` is not [Source](##Source) and from_source is not 'game' or 'strings'
    * **InvalidCategoryError**: name of category not in specified source

* unit
  * argument
    * **from_category**([str](https://docs.python.org/3/library/stdtypes.html#str), [Category](##Category)): if `type(from_category)` is not [Category](##Category) and source_name has specified, a Category object will auto generate
    * **name**([str](https://docs.python.org/3/library/stdtypes.html#str)): name of unit
    * **source_name**([str](https://docs.python.org/3/library/stdtypes.html#str)): when `type(from_category)` is not [Category](##Category), this argument can't be None
  * return
    * [Unit](##Unit) object
  * error
    * **InvalidSourceError**: only raise when `type(from_category)` is not [Category](##Category) and source_name is not 'game' or 'strings'
    * **InvalidCategoryError**: only raise when `type(from_category)` is not [Category](##Category) and from_category not in specified source_name
    * **InvalidUnitError**: name of unit not in specified category

## Classes
* [Source](###Source)
* [Category](##Category)
* [Unit](##Uni)

### Source
* attributes
  * **name**: name of source
  * **data**: raw source data([dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) type)
  * **dict**: formated source data([dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) type)
    * pattern: `name: category`
  * **list**: all the categories this source have
  * **categories**: all categories **NAME** in the source
* usage
  * for/while loop

### Category
* common attributes
  * **name**: name of category
  * **data**: raw category data([dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) type)
  * **list**: all units or element in the category
* attributes when `type(data)` is ListUnit
  * **dict**: formated category data([dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) type)
    * pattern: `num: unit` or `name: unit` or `title: unit`
  * **units**: all units **NAME** in the category
* attributes when `type(data)` is dict
  * **dict**: formated category data([dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) type)
    * pattern: `key: value`
  * **keys**: all keys in the category
* attributes when `type(data)` is list
  * **dict**: formated category data([dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) type)
    * pattern: `num: element`
  * **element**: all element in the category

### Unit
* common attributes
  * data: raw unit data([dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) type)
  * category: category that the unit belong
