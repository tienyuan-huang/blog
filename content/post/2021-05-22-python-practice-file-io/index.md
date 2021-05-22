---
title: 'python practice: 檔案IO'
author: 黃天原
date: '2021-05-22'
slug: python practice-file-io
categories:
  - programming
tags:
  - python
  - 練習
---

紀錄一下 python file io 的練習。  

## 寫入

首先是 file 寫入的部份。首先要用 `open()` 這個函數，與要讀入或寫入的檔案建立連結，指派成 物件`f` 。接著再用 `f` 的 method 來操作文件，用 `f.write("str")` 把要寫入的字串寫進 `f` 裡面。完成對 `f` 的動作之後，要記得用 `f.close()` 結束與文件的連結。  

當然，也可以用 `with open('No_Party_For_Cao_Dong.txt', 'w') as f:` 這樣的寫法來寫，寫完之後就會自動 close 。
```python


f = open('No_Party_For_Cao_Dong.txt', 'w')
print(type(f))

f.write('是為了什麼而流著血\n')
f.write('是為了誰而流眼淚\n')
f.write('我躲在夜裡去笑著黑\n')
f.write('因為沒有人能殺死鬼\n')

f.close()

# 用 `with open() as f:` 的寫法
with open('No_Party_For_Cao_Dong.txt', 'w') as f:
    f.write('''\
是為了什麼而流著血
是為了誰而流眼淚
我躲在夜裡去笑著黑
因為沒有人能殺死鬼
        ''')
        
```

## 讀入

接著是讀入。要讀入的話，記得 `open(file, mode = 'r')` ，`mode` 這個參數要設成 `'r'` （ read ）。接著再用 `f.read()` 這個 method 讀入。可以看到讀入之後，`type(f)`的結果，說明他是 `<class '_io.TextIOWrapper'>` 這個物件。當然可以用 `dir(f)` 查看他有哪些 attribute 跟 method 。

用 `f.read()` 讀入的檔案會是一個字串，可以從`type(content)` 的結果看到。

```python
with open('No_Party_For_Cao_Dong.txt', 'r') as f:
    print(type(f))
    content = f.read()
    print(content)
    print(f'type of f.read(): {type(content)}')

# <class '_io.TextIOWrapper'>
# 是為了什麼而流著血
# 是為了誰而流眼淚
# 我躲在夜裡去笑著黑
# 因為沒有人能殺死鬼

# type of f.read(): <class 'str'>

```

如果用 `f.readline()` 的方式讀入的話，一次只會讀入一行字串。

```python
with open('No_Party_For_Cao_Dong.txt', 'r') as f:
    print(f.readline())
    print(f.readline())
    print(f'type of f.readline(): {type(f.readline())}')

# 是為了什麼而流著血

# 是為了誰而流眼淚

# type of f.readline(): <class 'str'>
```

如果用 `f.readlines()` 的方式，則會把檔案讀入成一個 list 。

```python
with open('No_Party_For_Cao_Dong.txt', 'r') as f:
    content = f.readlines()
    print(content)
    print(f'type of `f.readlines()`: {type(content)}')

# ['是為了什麼而流著血\n', '是為了誰而流眼淚\n', '我躲在夜裡去笑著黑\n', '因為沒有人能殺死鬼\n']
# type of `f.readlines()`: <class 'list'>
```

無論是 `f` 或是 `f.readlines()` 出來的 list ，都可以放到 `for loop` 中作為 iterator 。

```python

with open('No_Party_For_Cao_Dong.txt', 'r') as f:
    for line in f.readlines():
        print(line, end="")

# 是為了什麼而流著血
# 是為了誰而流眼淚
# 我躲在夜裡去笑著黑
# 因為沒有人能殺死鬼

with open('No_Party_For_Cao_Dong.txt', 'r') as f:
    for line in f:
        print(line, end="")

# 是為了什麼而流著血
# 是為了誰而流眼淚
# 我躲在夜裡去笑著黑
# 因為沒有人能殺死鬼

```