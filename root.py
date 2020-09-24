#!/usr/bin/env python
# coding: utf-8

# # NetFlix data sets

# A time series is a series of data points indexed (or listed or graphed) in time order. Most commonly, a time series is a sequence taken at successive equally spaced points in time.

# In[1]:


import pandas as pd


# ## Importing data sets from site https://finance.yahoo.com/quote/NFLX/history?period1=1569319583&period2=1600941983&interval=1d&filter=history&frequency=1d

# In[2]:


netflix=pd.read_csv('/home/rabinrajgautam/Downloads/ML AI/NFLX.csv')


# ### Reading first 5 lines using head()

# In[5]:


netflix.head()


# ### Reading last 5 lines using tail()

# In[6]:


netflix.tail()


# In[7]:


netflix.columns


# In[8]:


netflix.shape


# In[12]:


type(netflix.Date[0])


# ### Since the 'Date' column is in string, we need to convert into date format using parse_dates

# In[37]:


netflix=pd.read_csv('/home/rabinrajgautam/Downloads/ML AI/NFLX.csv', parse_dates=['Date'])


# In[38]:


netflix


# ### Now changing the Date into index of our table using index_col='Date'

# In[39]:


netflix.set_index('Date', inplace=True)


# ### Checking the index values using index 

# In[40]:


netflix.index


# ### Checking how many null values are present. 

# In[34]:


netflix.isnull().sum()


# ### It is found that there are 0 null values !

# ### Now just looking at the Jan data only using index 2020-01

# In[47]:


netflix['2020-01'].head()


# ### The mean of the 'Close' column using mean()

# In[50]:


netflix['2020-01'].Close.mean()


# ### Calculating the mean of 'Close' column based on Month !

# In[61]:


netflix.Close.resample('M').mean()


# ### Plotting these mean values 

# In[62]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[68]:


netflix.Close.resample('M').mean().plot()


# ### From this graph we conclude that, in months : From  Jul to Sep 2020 , the values are maximum.

# ### Visualizing the graph in bar below:
# 

# In[80]:


netflix.Close.resample('M').mean().plot(kind='bar')


# ### We can resample base on quaterly, weekly also, insted of Month 'M' , we can write 'Q' for quaterly and 'W' for weekly, which is shown below :

# In[77]:


netflix.Close.resample('Q').mean().plot(kind='bar')


# ## Resampling generates a unique sampling distribution on the basis of the actual data. We can apply various frequency to resample our time series data. This is a very important technique in the field of analytics. To reduce the granularity we have introduce the term resample here.

# In[ ]:




