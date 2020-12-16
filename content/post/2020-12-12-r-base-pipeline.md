---
title: R base的內建pipeline
author: deadfate-sky
date: '2020-12-12'
slug: r-base-pipeline
categories:
  - programming
tags:
  - R
  - 乾貨
---

今天意外看到R core team也有在開發它們自己內建的pipeline，嚇得我趕緊下載了R的dev版本。R base版本的pipeline，長成```|>```這附模樣，可以看到像下面那篇twitter的例子。[^add html]

<blockquote class="twitter-tweet"><p lang="en" dir="ltr"><a href="https://twitter.com/hashtag/RStats?src=hash&amp;ref_src=twsrc%5Etfw">#RStats</a> community, really? It&#39;s been like 5 hours now and no one noticed the big news? 😛<a href="https://t.co/c4OXTO0WCw">https://t.co/c4OXTO0WCw</a><br><br>Thank you <a href="https://twitter.com/LukeTierney4?ref_src=twsrc%5Etfw">@LukeTierney4</a> <a href="https://twitter.com/_lionelhenry?ref_src=twsrc%5Etfw">@_lionelhenry</a> <a href="https://twitter.com/jimhester_?ref_src=twsrc%5Etfw">@jimhester_</a> (who else?)<a href="https://twitter.com/hashtag/pipypipy?src=hash&amp;ref_src=twsrc%5Etfw">#pipypipy</a> <a href="https://t.co/5P9QPe1H8a">pic.twitter.com/5P9QPe1H8a</a></p>&mdash; Henrik Bengtsson (@henrikbengtsson) <a href="https://twitter.com/henrikbengtsson/status/1334703130378788866?ref_src=twsrc%5Etfw">December 4, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

裝好R-dev版本之後，我很快的找了關於```|>```的help document來看看。
![R-pipeline-help](/img/R-pipe-doc.png)
![R-pipeline-example](/img/R-pipe-ex.png)
文檔大致上長得如此，這個內建pipe的方法，就跟熟悉的```%>%```一樣，例如：
```r
> mtcars |> subset(cyl == 4) |> subset(select = mpg)
> 
                mpg
Datsun 710     22.8
Merc 240D      24.4
Merc 230       22.8
Fiat 128       32.4
Honda Civic    30.4
Toyota Corolla 33.9
Toyota Corona  21.5
Fiat X1-9      27.3
Porsche 914-2  26.0
Lotus Europa   30.4
Volvo 142E     21.4
```
就可以得到選出來的結果，看看cyl是4的車子，它的mpg是多少。其效果跟```{dplyr}```的```filter()```、```select()```一樣，只是現在全部都能用內建的函數完成。

另外，它也能讓pipeline直接進到function裡面，像是下面這樣
```r
> mtcars |> subset(cyl == 4) |> \(d) lm(mpg ~ disp, data = d)

Call:
lm(formula = mpg ~ disp, data = d)

Coefficients:
(Intercept)         disp  
    40.8720      -0.1351 
```
把選好的data.frame放進一個可以生成model的function裡面，效果跟
```mtcars |> subset(cyl == 4) |> function(d) lm(mpg ~ disp, data = d)```

一樣。

總結來說，R core team開發這個內建的水管，真是個酷東西。

[^add html]: 因為在內嵌html的時候遇到一些困難，Hugo有問題，所以附上解決方案<https://stackoverflow.com/questions/63198652/hugo-shortcode-ignored-saying-raw-html-omitted>