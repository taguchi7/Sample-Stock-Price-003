#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandas_datareader import data
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = data.DataReader('7269.JP','stooq')


# In[3]:


df.head()


# In[4]:


df = df.sort_index()


# In[5]:


df.head()


# In[6]:


df.index.min()


# In[7]:


df.index.max()


# In[8]:


df.index>='2016-03-23 00:00:00'


# In[9]:


df[df.index>='2016-03-23 00:00:00']


# In[10]:


df[df.index<='2021-03-19 00:00:00']


# In[11]:


df[(df.index>='2016-03-23 00:00:00') & (df.index<='2021-03-19 00:00:00')]


# In[12]:


df = df[(df.index>='2016-03-23 00:00:00') & (df.index<='2021-03-19 00:00:00')]


# In[14]:


date=df.index
price=df['Close']

span01=5
span02=25
span03=50

df['sma01'] = price.rolling(window=span01).mean()
df['sma02'] = price.rolling(window=span02).mean()
df['sma03'] = price.rolling(window=span03).mean()

plt.figure(figsize=(30,15))
plt.subplot(2,1,1)

plt.plot(date,price,label='Close',color='#99b898')
plt.plot(date,df['sma01'],label='sma01',color='#e84a5f')
plt.plot(date,df['sma02'],label='sma02',color='#ff847c')
plt.plot(date,df['sma03'],label='sma03',color='#feceab')
plt.legend()

plt.subplot(2,1,2)
plt.bar(date,df['Volume'],label='Volume',color='grey')
plt.legend()


# In[ ]:




