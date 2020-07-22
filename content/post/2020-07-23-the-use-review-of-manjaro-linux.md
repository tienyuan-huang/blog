---
title: manjaro linux 使用心得
author: deadfate-sky
date: '2020-07-23'
slug: the-use-review-of-manjaro-linux
categories:
  - programming
tags:
  - 乾貨
  - 認真
---



近日把不久前才開始使用的ubuntu換成manjaro這個linux發行版。之所以會這麼做有一些小原因，像是如果我用ubuntu跑Path of Exile就完全沒辦法用其他程式，這樣我要查別人的build抄作業很麻煩，所以就換了（？？？？這什麼啦機理由？？？）。 

於是我就愉快的換系統啦！  


先看個留作紀念的ubuntu系統資訊  

```shell
evan19983314@evan19983314-X556UR:~$ screenfetch
                          ./+o+-       evan19983314@evan19983314-X556UR
                  yyyyy- -yyyyyy+      OS: Ubuntu 20.04 focal
               ://+//////-yyyyyyo      Kernel: x86_64 Linux 5.4.0-40-generic
           .++ .:/++++++/-.+sss/`      Uptime: 2h 3m
         .:++o:  /++++++++/:--:/-      Packages: 2662
        o:+o+:++.`..```.-/oo+++++/     Shell: bash
       .:+o:+o/.          `+sssoo+/    Resolution: 1920x1080
  .++/+:+oo+o:`             /sssooo.   DE: GNOME 3.36.3
 /+++//+:`oo+o               /::--:.   WM: Mutter
 \+/+o+++`o++o               ++////.   WM Theme: Adwaita
  .++.o+++oo+:`             /dddhhh.   GTK Theme: Yaru [GTK2/3]
       .+.o+oo:.          `oddhhhh+    Icon Theme: Yaru
        \+.++o+o``-````.:ohdhhhhh+     Font: Ubuntu 11
         `:o+++ `ohhhhhhhhyo++os:      Disk: 115G / 226G (54%)
           .o:`.syhhhhhhh/.oo++o`      CPU: Intel Core i5-6198DU @ 4x 2.8GHz [53.0°C]
               /osyyyyyyo++ooo+++/     GPU: GeForce 930MX
                   ````` +oo+++o\:     RAM: 3991MiB / 7829MiB
                          `oo++.      
evan19983314@evan19983314-X556UR:~$
```

在來看一下新的manjaro  
![manjaro](https://i.imgur.com/iQLbajQ.png) 


## 為何從ubuntu到manajro
最一開始是被這篇文章燒到：[为什么我抛弃了 Ubuntu？](https://www.chainnews.com/articles/242900708378.htm)，他說manjaro的整個系統的應用，還有desktop envirment都是已經輕量、低耗為目的，這個特色深深的吸引了我（作為一個因為FB app太肥而去用FB lite 忍受超級小字的人）。也確實，ubuntu預設的gnome桌面會一直偷吃我的讀顯內存，大概有事沒事幾十到一兩百MB，這也讓我有了「搞不好換個偷吃顯卡少一點的系統跑遊戲會順一點」的念頭。   

就在這個大膽的想法中，我就大概背備份了10G的重要內容，勇敢的換下去了。  

在細談安裝之前，也順便提一下linux的各大發行版好了。在現在這個時間，2020，linux其實有了相當多的發行版，而且對terminal新手算是非常友善。像ubuntu，記一記apt install之類的指令，可以完成超級多事情，使用terminal沒有想像中的困難。可以參考一下[維基百科的介紹](https://zh.wikipedia.org/wiki/Linux%E5%8F%91%E8%A1%8C%E7%89%88)

那就開始介紹manjaro吧。那其實網路上的介紹很豐富，中文世界也找得到一定量的資訊，我就不多提了，給一些網址。

* 官網： <https://manjaro.org/>
* wiki:<https://zh.wikipedia.org/wiki/Manjaro_Linux>  


然後呢，當初我是看著一些文章跟yt setup的，所以也把這些參考資料貼上來。  

* 青鳥脈搏：<https://archer1609wp.wordpress.com/2018/04/29/manjaro-first-look/>  
這個blog寫了滿多關於manjaro的東西的，如果在google搜尋某些資訊，用中文一定很容易搜到這個blog XD。像這篇 [Manjaro字型設定折騰記（上）](https://archer1609wp.wordpress.com/2018/10/23/manjaro-font-config-1/)

* manjaro踩坑记：<https://mrswolf.github.io/zh-cn/2019/05/24/manjaro%E8%B8%A9%E5%9D%91%E8%AE%B0/index.html>
* Manjaro Linux 踩坑調教記錄：<https://www.jishuwen.com/d/pfAm/zh-tw>
* manjaro xfce 18.0 踩坑记录：<https://juejin.im/entry/5da56cd56fb9a04e223330ac#_label8_0>

這幾個應該都是西岸國人發的文章，如何安裝、如何設置包管理器都介紹的非常詳細，大推。  


再來放一些影片類的：

* Installing Nvidia drivers on a fresh install of Majaro Arch Linux: <https://youtu.be/ea5sgVImGmA>  
雖然這是2019的影片，但基本上manjaro的圖形安裝界面就是這樣走，沒什麼大坑。  

* How To Set Up Manjaro 19 KDE Edition For Gaming: <https://youtu.be/ibge7-4sitQ>  
對我這樣一個（雲）玩家而言，能夠遊戲的當然非常重要，照著這個影片操作，基本上就能把玩遊戲需要的各式平台跟套件，像**steam**、linux上知名的**lutris**，跟想執行一些windows才能完的遊戲必裝的**wine**，通通都可以在manjaro用套件管理器點擊安裝。當然，用terminal也可以很快的裝好。   

之後預計也會在寫幾篇文，談談怎麼在manjaro或其他linux發行版中設置遊戲環境，跟linux在2020這個年代，對遊戲的支援是如何地突飛猛進。


參考資料放完，就簡單再把一些對我比較重要的資訊貼出來。  

## 一些安裝後的配置  
首先當然是先把東西套件更新更新

```shell
pacman -Syu 
```
manjaro是用pacman這個套件管理器，跟ubuntu的apt指令不大一樣，但邏輯上都差不多。順便附上指令參考的兩個文章。
<https://www.jishuwen.com/d/pfAm/zh-tw>  
<https://www.cnblogs.com/kirito-c/p/11181978.html>  

```shell
pacman -Syu                   # 升級整個系統，y 是更新資料庫，yy 是強制更新，u 是升級軟體
pacman -S package_name  安裝套件
pacman -R package_name  移除套件
```

記得先安裝pamac這個圖形界面的套件管理器
```shell
pacman -S pamac
```
對了，pacman的指令前面記得加個```sudo```，用root的權限才能安裝跟移除套件。  

因為manjaro是使用arch linux為底，所以也可以使用AUR的套件庫，詳情可以參照一下[AUR wiki](https://wiki.archlinux.org/index.php/Arch_User_Repository_(%E6%AD%A3%E9%AB%94%E4%B8%AD%E6%96%87))

在pacman裡可以在設置中設定納入AUR的套件庫，用指令的話，通常都會透過一些幫手套件，會比pacman的命令還要方便，像是```yay```之類的。

```shell
sudo pacman -S yay
```
然後yay的指令基本上跟pacman差不多
```shell
yay -S package_name
```

**裝個輸入法**  
```shell
# 我是用fcitx
sudo pacman -S fcitx fcitx-chewing
# 對不同 GUI 框架的支援，全部安裝
sudo pacman -S fcitx-im
# 圖形化配置介面
sudo pacman -S fcitx-configtool
```
設定一下
``` shell
vim ~/.xprofile
```
這邊要稍微知道vim怎麼使用
```
GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
XMODIFIERS=@im=fcitx
```
設定完就應該可以用了！不行的話在上網搜尋一下


## 安裝需要用的套件  

**安裝R語言**  
對，我需要裝
```shell
sudo pacman -S r
```


這邊真的要稱讚一下，基本上需要任何東西，都能在manjaro的pacman或AUR宇宙找到，而且版本基本上滿新的。不用像ubuntu，某些東西要連到[PPA](https://zhuanlan.zhihu.com/p/55250294)才裝得進去，有好有壞啦。

**Rstudio**  
裝完R通常都用這個ide，很不巧的是rstudio官方自己沒有提供manajro的官方安裝檔，所以要去AUR找。
```shell
yay -S rstudio-desktop-git
```
<https://aur.archlinux.org/packages/rstudio-desktop-git/> 

對了，到這邊才想起來，上述有關安裝的指令，基本上都能在pamac用「搜尋—安裝」的方式完成！只是我習慣用terminal安裝，這樣一旦有錯誤，也比較好找出問題解決。  

然後這邊要特別提一下，我的rstudio是裝rstudio-desktop-git版的，應該就是直接從github抓檔案下來make？我也不清楚，但我試過rstudio-desktop跟rstudio-desktop-bin兩種版本，一個是一點進去就crash，另一個是用了10分鐘也crash，所以建議還是用git版的，相對穩定。


**miniconda**  
我用python習慣用miniconda來裝，因為這樣後面要裝tensorflow-gpu跟python的intel發行版都比較方便。  

```shell
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh  

bash Miniconda3-latest-Linux-x86_64.sh
```  
然後一路裝到底就好，記得查一下怎麼把自動進入base的環境取消掉。  

關於tensorflow-gpu如何安裝，我在[GCP初體驗](https://deadfate.rbind.io/2020/07/09/google-cloud-platform-first-experience/)有說過。用conda安裝的話，會自動幫你裝上相依的cuDnn跟cuda toolkit，就不用像用pip安裝一樣，還要自己確認這些東西的版本。

除了tensorflow之外，我也會用conda安裝[intel發行的python](https://software.intel.com/content/www/cn/zh/develop/articles/using-intel-distribution-for-python-with-anaconda.html) ，就是嚐個鮮跟爽。  

不過intel-python的tensorflow好像不錯，在跑一些比較小的DL訓練，像是經典的mnist，如果層數跟neural都不多的話，intel-python會比我的nvidia 930mx還要快很多。（我不知道為什麼每次要用GPU的時候，在set model的那個階段```model = keras.Sequential()```都會跑瞎雞巴久。  


## 結語  
好啦！簡單的intro就到這邊，之後會再提一些關於遊戲設置跟安裝的部份。
