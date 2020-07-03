#!/usr/bin/env python
# coding: utf-8

# In[87]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')
sns.set_style("whitegrid")
plt.style.use("fivethirtyeight")


# In[4]:


get_ipython().system('dir')


# In[25]:


listing_df = pd.read_csv('C:\\Users\\Hiba\\AB_NYC_2019.csv')


# In[26]:


print(listing_df)


# In[29]:


listing_df.isnull().sum()


# In[8]:


listing_df = pd.read_csv('C:\\Users\\Hiba\\AB_NYC_2019.csv').head()


# In[13]:


import pandas as pd


# In[17]:


listing_df = pd.read_csv('C:\\Users\\Hiba\\AB_NYC_2019.csv')


# In[18]:


listing_df.head()


# In[19]:


listing_df.isnull().sum


# In[24]:


listing_df.info()


# ##checking the missing value## 

# In[28]:


listing_df.isnull().sum()


# In[ ]:





# In[35]:


for column in listing_df.columns:
    if listing_df[column].isnull().sum() !=0:
         print("=======================================================")
         print(f"{column} ==> Missing Values : {listing_df[column].isnull().sum()}, dtypes : {listing_df[column].dtypes}")


# For the float dtypes we are going to fill the missing values by mean(), for object we are going to fill missing values by mode(). last_review is a date, so we need to convert it, then fill missing values from previous values.
# 

# In[42]:


listing_df["last_review"] = pd.to_datetime(listing_df.last_review)


# In[43]:


listing_df.last_review.isnull().sum()


# In[45]:


listing_df["reviews_per_month"] = listing_df["reviews_per_month"].fillna(listing_df["reviews_per_month"].mean())
listing_df.tail()




# In[50]:


listing_df.last_review.fillna(method="ffill", inplace=True)


# In[54]:


for column in listing_df.columns:
    if listing_df[column].isnull().sum() != 0:
        print("=======================================================")
        print(f"{column} ==> Missing Values : {listing_df[column].isnull().sum()}, dtypes : {listing_df[column].dtypes}")


# In[57]:


for column in listing_df.columns:
    if listing_df[column].isnull().sum() != 0:
        listing_df[column] = listing_df[column].fillna(listing_df[column].mode()[0])


# In[58]:


listing_df.isnull().sum()


# In[63]:


pd.options.display.float_format = "{:.2f}".format
listing_df.describe()


# In[64]:


categorical_col = []
for column in listing_df.columns:
    if len(listing_df[column].unique()) <= 10:
        print("===============================================================================")
        print(f"{column} : {listing_df[column].unique()}")
        categorical_col.append(column)


# 
# 
# # Drop ["id", "host name"] because it is indignificant and also for ethical reasons 
# listing_df.drop("id","host name"), axis = "columns", inplace= True)

# In[76]:


listing_df.drop(["id", "host_id"], axis="columns", inplace=True)
listing_df.head()


# In[77]:


listing_df.last_review.isnull().sum()


# ## Data Visualization ##

# In[85]:


listing_df.hist(edgecolor="black", linewidth=1.2, figsize=(30, 30));


# In[89]:


plt.figure(figsize=(30, 30))
sns.pairplot(listing_df, height=3, diag_kind="hist")


# ## Our observation after checking the graphic ## 
# 
# -latitude and longitude have a normal distribution, most of the hosts are concetrated in specific area.
# -reviews_per_month has a lot of outlayers, because of the missing values filled by mean() and mode()
# -availability_365 the most of the hosts are not available all the year.
# 

# In[91]:


col = list(listing_df.columns)
col.remove("latitude")
col.remove("longitude")


# In[93]:


print(col)


# In[94]:


categorical_col


# In[95]:


sns.catplot("neighbourhood_group", data=listing_df, kind="count", height=8)


# In[99]:


sns.set(font_scale=1.5)
sns.catplot("room_type", data=listing_df, kind="count", height=8)

