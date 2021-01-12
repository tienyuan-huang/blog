---
title: 深度學習、神經網絡、吳恩達跟李宏毅
author: 黃天原
date: '2020-07-13'
slug: deep learning neural network Andrew Ng Hung-yi Lee
categories:
  - statistic
tags:
  - 乾貨
  - 認真
---

這幾天認真看了很多影片之後，總算大致把最最最最基礎的神經網絡運作方式，了解了個大概，摁，就很101、很入門的大概。  

先丟幾個之前再學習機器學習時，有使用到的資源。  
[李宏毅老師-機器學習](https://www.youtube.com/playlist?list=PLJV_el3uVTsPy9oCRY30oBPNLCo89yu49)  

[吳恩達Andrew Ng](https://www.youtube.com/playlist?list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN)  

我這次熱血開看的時候，剛好搭上暑假Tony老師開的讀書會，主要是搭著[deep learning with R](https://www.manning.com/books/deep-learning-with-r) 這本書，然後我自己再加上[三藍一棕](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) 的影片配著看。兩點題外話，deep learning with R的作者是鼎鼎大名的[J.J. Allaire](https://rstudio.com/speakers/j.j.-allaire/)-Rstudio的創辦人跟現在的CEO；而三藍一棕則是超級讚的數學視覺教學影片，它把超多數學、統計的概念用視覺化的方式呈現，不喜歡看公式的人，可以先看看它那邊有沒有相關主題的影片可看，看完再看公式，或許會比較好吸收。

好啦，回到主題。因為大致知道了deep learning的入門架構，所以知道說為什麼李宏毅老師跟吳恩達在課程安排上會是這樣。就是可能做個intro、提個variance bias tradeoff之後，就開始講linear regression，而且會提到cost(loss) function、gradient decent這些東西。我第一次看這些影片的時候，是想自學機器學習，所以就沒看後面關於神經網絡的部份，自然就很難理解為什麼在提linear regression, logistic的時候，要特別用gradient decent這種方法，不是公式一解就出來了嗎？統計101都有學過阿？後來才知道，原來這是為後面的神經網絡做準備。  

因為通常介紹neural network，都是用 [MNIST](https://en.wikipedia.org/wiki/MNIST_database) 這個手寫數字的資料集，用手寫辨識當作入門介紹，所以在第一個到的神經網絡裡面，每個神經元的函數就用logistic，這樣最後才會回傳0~1之間的數字，然後可能再加上一些bias，或者說用[ReLU](https://zh.wikipedia.org/wiki/%E7%BA%BF%E6%80%A7%E6%95%B4%E6%B5%81%E5%87%BD%E6%95%B0)當作激勵函數。而當所有神經元連起來之後，我們整個神經網絡的參數Beta跟bias，應該會是多到無法計算，不像在統計學上linear regression的時候，只用一個x預測y，只要算出Beta0, Beta1就完成了。這時候，gradient decent這樣可以處理大量參數的估計方法，就顯得非常重要了。  

所以，其實李宏毅老師跟吳恩達的課程設計前半部份，是為了講神經網絡，才先講那些知識點。如果今天學習的目標不是深度學習，而是其他的機器學習模型，那我會推薦[Introduction to Statistical Learning](http://faculty.marshall.usc.edu/gareth-james/ISL/) 作為入門的課本，再加上作者本人的 [網路課程](https://www.youtube.com/playlist?list=PLOg0ngHtcqbPTlZzRHA2ocQZqB1D_qZ5V)。有些人也會推林宣田老師的[機器學習基石](https://www.youtube.com/watch?v=nQvpFSMPhr0&list=PLXVfgk9fNX2I7tB6oIINGBmW50rrmFTqf)，有興去的人，可以選擇適合自己的課程試試。  

不過，深度學習、人工智慧，可以算是機器學習的一個子集吧，這兩個潮潮的東西也是有很多概念是重疊的，也沒有說應該先學哪一種會比較好。
