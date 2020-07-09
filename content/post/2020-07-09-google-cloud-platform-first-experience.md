---
title: google cloud platform 初體驗
author: deadfate
date: '2020-07-09'
slug: google cloud platform First Experience
categories:
  - statistic
  - programming
tags:
  - R
  - python
---
因為暑假參加了Tony老師的工作坊，剛好有機會試試google cloud platform這個東西。google cloud platform又簡稱GCP，跟google cloud drive不一樣，主要是提供雲端運算、資料庫架設、伺服器這些需要主機、OS、GPU這些設備的服務。  

GCP就跟微軟的[Azure](https://aws.amazon.com/tw/) 、[Amazon web services](https://aws.amazon.com/tw/) 一樣，都是提供這些服務的平台，只是作為網路時代起家的google，在這部份的業務上其實落後微軟跟Amazon不少。也正因為這樣，google也很努力的宣傳他們自家的GCP。  

那就直接進入GCP的使用吧！我是使用他們的compute engine，網路上有很多關於如何填信用卡認證、如何開一台虛擬主機（Virtual Machine）的教學，他們的介面也有使用指引，看一看應該就能成功開啟了。google很佛心的提供了300鎂的免費額度試用，可以用滿久的。  


## 安裝GPU driver、tensorflow跟其他需要的東西  
主機位置挑哪裡都可以，反正有GPU的地方就好。我的系統是選擇ubuntu 20.04，因為自己的筆電也是用這個系統（有空也來寫一篇灌系統的心得），cpu選8顆，因為要8顆才能選GPU。硬碟記得選個20G，因為10G很容易滿。GPU的話隨便挑，價格有差，但應該沒差太多，反正都是Nvidia。  

大致節錄一下資訊
* CPU
```shell
xxxxxxxxxxxx@instance-1:~$ lscpu
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
Address sizes:                   46 bits physical, 48 bits virtual
CPU(s):                          8
On-line CPU(s) list:             0-7
Thread(s) per core:              2
Core(s) per socket:              4
Socket(s):                       1
NUMA node(s):                    1
Vendor ID:                       GenuineIntel
CPU family:                      6
Model:                           79
Model name:                      Intel(R) Xeon(R) CPU @ 2.20GHz
Stepping:                        0
CPU MHz:                         2200.000
BogoMIPS:                        4400.00
Hypervisor vendor:               KVM
Virtualization type:             full
L1d cache:                       128 KiB
L1i cache:                       128 KiB
L2 cache:                        1 MiB
L3 cache:                        55 MiB
NUMA node0 CPU(s):               0-7
```  

* GPU
```shell

xxxxxxxx@instance-1:~$ nvidia-smi
Thu Jul  9 10:02:27 2020       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 440.100      Driver Version: 440.100      CUDA Version: 10.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla P100-PCIE...  Off  | 00000000:00:04.0 Off |                    0 |
| N/A   34C    P0    25W / 250W |     74MiB / 16280MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0      1011      G   /usr/lib/xorg/Xorg                            61MiB |
|    0      1359      G   /usr/bin/gnome-shell                          12MiB |
+-----------------------------------------------------------------------------+
```

* 記憶體

```shell
xxxxxxxx@instance-1:~$ free -h
              total        used        free      shared  buff/cache   available
Mem:           29Gi       564Mi        27Gi       1.0Mi       1.1Gi        28Gi
Swap:            0B          0B          0B
```

* 硬碟
```shell
xxxxxxx@instance-1:~$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        19G  9.6G  8.7G  53% /
devtmpfs         15G     0   15G   0% /dev
tmpfs            15G     0   15G   0% /dev/shm
tmpfs           3.0G  1.2M  3.0G   1% /run
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs            15G     0   15G   0% /sys/fs/cgroup
/dev/sda15      105M  3.9M  101M   4% /boot/efi
/dev/loop0       55M   55M     0 100% /snap/core18/1754
/dev/loop2       72M   72M     0 100% /snap/lxd/15896
/dev/loop1      118M  118M     0 100% /snap/google-cloud-sdk/139
/dev/loop3       30M   30M     0 100% /snap/snapd/8140
tmpfs           3.0G   20K  3.0G   1% /run/user/123
/dev/loop4       72M   72M     0 100% /snap/lxd/16044
/dev/loop5      118M  118M     0 100% /snap/google-cloud-sdk/140
tmpfs           3.0G  4.0K  3.0G   1% /run/user/1001
```  
### 安裝nivida driver
先加入nvidia的repository

```shell
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update
```

尋找可用的driver
```shell
sudo apt-cache search nvidia-*
```

安裝
```shell
sudo apt install nvidia-driver-440
```
因為我是找到nvidia-driver-440，所以就裝了這版的驅動。需要注意的事，tensor的版本跟nvidia驅動、CUDA、cuDNN這3個東西的版本有互相依賴,所以記得查一下。我裝tensorflow 2.1.0，440版本的是可以執行的。

### 安裝miniconda、tensorflow
因為我要用conda來安裝tensorflow，所以先安裝miniconda。先去他們的[官網](https://docs.conda.io/en/latest/miniconda.html) 最新的安裝包，然後```wget```下載。

```shell
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```
再來直接執行他 
```shell
bash Miniconda3-latest-Linux-x86_64.sh
```  

安裝好了之後，就直接使用```conda```安裝tensorflow。[這篇文章](https://zhuanlan.zhihu.com/p/46579831) 有說明為什麼用conda裝比較好。速度快不快我不確定，不過像是 CUDA和cuDNN他也會一併幫你裝好，省下在那邊對照版本的時間。  

```shell
conda install tensorflow-gpu
conda install keras
```

裝完之後，就打開python確認一下有沒有安裝好吧！需要注意的是，因為我安裝的是tensorflow2.1.0，所以語法跟tensorflow1有點不一樣
```python
import tensorflow as tf
print(tf.__version__)
print(tf.config.list_physical_devices('GPU'))
```
最後回傳```TRUE```就代表有  

接下來就可以開始試試train model了！