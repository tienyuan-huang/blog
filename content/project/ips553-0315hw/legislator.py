#!/usr/bin/env python
# coding: utf-8

# ## 1. 資料讀入, 預處理

# In[1]:


import pandas as pd
fb = pd.read_csv('nysu_10902_2019_research_right.csv')
politics = pd.read_csv('9th_legislator_promise.csv')


# In[2]:


fb.head(1)


# In[3]:


# 查看立委名冊
politics.head()


# In[4]:


politics.姓名.unique()


# In[5]:


fb.page_name.unique()


# ## 2. 使用呂孫綾作為查看對象

# In[6]:


lu = fb.loc[fb.page_name == '呂孫綾']
lu.head()


# In[7]:


lu.loc[lu.created_time_taipei == max(lu.created_time_taipei),
      "created_time_taipei"]
# 蒐到的fb資料中，最晚的日期是`2019-12-11T12:33:58+0000`


# In[8]:


lu.loc[lu.created_time_taipei == min(lu.created_time_taipei),
      "created_time_taipei"]
# 蒐到的fb資料中，最早的日期是 `2019-01-03T14:19:05`


# In[9]:


lu.loc[:,'new_date'] = pd.to_datetime(lu['created_time_taipei']).dt.date
lu.loc[:,'month_year'] = pd.to_datetime(lu['new_date']).dt.to_period('M')


# In[10]:


lu['new_date'].value_counts()


# In[11]:


lu['month_year'].value_counts()


# In[12]:


lu.head()


# ## 3. 將 `lu` 的欄位，按照月份groupby後加總

# 即可計算出呂孫綾的每月聲量數值

# In[13]:


## 先再看一次 `lu` 的每個欄位
lu.head(1)


# In[14]:


results = lu.groupby('month_year').sum()
results


# 稍微了解一下 `like_count`,`share_count`,`comment_count` 這三個等等會視覺化觀察的指標

# In[15]:


results.loc[:,['like_count','share_count','comment_count']].describe()


# In[16]:


results.loc[:,['like_count','share_count','comment_count']].agg([min,max])


# In[17]:


results.index.name = 'newhead'
results.reset_index(inplace=True)
results.head()


# In[18]:


tmp = results['newhead'].map(str)
isinstance(tmp[0],str)
## 將`newhead`轉為str, 準備作為圖片label


# ## 4. 將呂孫綾每月 fb 聲量視覺化

# In[44]:


import matplotlib.pyplot as plt

labels = results['newhead'].map(str)
width = 0.5       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots(1,1)
fig.set_size_inches(15, 8)

ax.bar(labels, results['like_count'], width, label='like_count')
ax.bar(labels, results['share_count'], width, label='share_count', bottom=results['like_count'])
ax.bar(labels, results['comment_count'], width, label='comment_count', bottom=results['share_count']+results['like_count'])

ax.legend()
plt.show()


# 可以觀察到，呂孫綾的臉書聲量顯然是隨著選舉熱度逐漸升高。
# 而綜合選前的時事，我決定觀察兩個重點
# 
# 1. 呂孫綾上館長節目是在11/23
# 2. 12的聲量為何突然跌落

# In[20]:


nov = lu.loc[lu.month_year == "2019-11"].groupby('new_date').sum()
nov.head()


# In[21]:


## 最多討論
nov.loc[nov.like_count == max(nov.like_count),['like_count']]


# In[22]:


nov.index.name = 'the_date'
nov.reset_index(inplace=True)
nov.head()


# In[23]:


len(nov['like_count'])


# In[24]:


nov.shape[0]


# In[46]:


#labels = nov.the_date.map(lambda i: str(i))
labels = [str(i) for i in range(1,nov.shape[0]+1)]

fig, ax = plt.subplots()
fig.set_size_inches(15, 8)

ax.plot(labels, nov['like_count'], label = 'like_count')
ax.plot(labels, nov['share_count'], label = 'share_count')
ax.plot(labels, nov['comment_count'], label = 'comment_count')

ax.legend()

plt.show()


# 較高的時間點有 8, 17, 23, 29這四天，因此我們依序取出這四天的文章來觀察
# 
# 我先將11月每天的發文總數計算出來，可以發現其實只有17號發了較多篇文章，另外三個聲量較高的日期，並沒有特別發比較多的臉書文。

# In[26]:


lu.loc[lu.month_year == '2019-11'].new_date.value_counts()


# 接著，再把8號發的文章內容取出檢視：

# In[34]:


lu.new_date.loc[:] = lu.new_date.map(lambda d: str(d))
mes = lu.loc[lu.new_date == '2019-11-08', "message"]
print(f'1.:\n{list(mes)[0]},\n\n2.:\n{list(mes)[1]}\n\n3.:\n{list(mes)[2]}')


# 在8號的文章，其實沒有什麼太特別的內容。
# 

# 在 11/23 號的按讚數量特別高，推測跟上館長的節目有關係。但這些讚的態度是「稱讚」還是「倒讚」，就必須看留言的內容才能決定。

# In[41]:


mes = lu.loc[lu.new_date == '2019-11-23', "message"]
print(f'文章數: {len(list(mes))}')
print(f'1.:\n{list(mes)[0]},\n\n2.:\n{list(mes)[1]}\n\n3.:\n{list(mes)[2]}')


# 11/29 的發文，也沒有太過於特別的內容。

# In[48]:


mes = lu.loc[lu.new_date == '2019-11-29', "message"]
print(f'文章數: {len(list(mes))}')
print(f'1.:\n{list(mes)[0]},\n\n2.:\n{list(mes)[1]}\n\n3.:\n{list(mes)[2]}')

