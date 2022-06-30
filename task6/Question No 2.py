
# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv("https://raw.githubusercontent.com/cognizance-amrita/AI-Tasks/main/Task-1/Q2-Dataset.csv")


# In[3]:


df.head()


# In[32]:


missing_value_formats = ["n.a.","?","NA","n/a", "na", "--"]
df = pd.read_csv("https://raw.githubusercontent.com/cognizance-amrita/AI-Tasks/main/Task-1/Q2-Dataset.csv", na_values = missing_value_formats)


# In[6]:


print(df.isnull().sum())


# In[7]:


df['LotFrontage'].fillna(1, inplace=True)


# In[8]:


print(df['LotFrontage'])


# In[9]:


print(df['Alley'].isnull())


# In[10]:


df['Alley'].fillna('no alley name mentioned', inplace=True)
print(df['Alley'])


# In[11]:


print(df['BsmtQual'].isnull())


# In[12]:


df[df['BsmtQual'].isnull()]


# In[33]:


df['BsmtQual'].fillna('3', inplace=True)


# In[14]:


df[df['BsmtQual'].isnull()]


# In[15]:


print(df['BsmtCond'].isnull())


# In[16]:


df[df['BsmtCond'].isnull()]


# In[34]:


df['BsmtCond'].fillna('78', inplace=True)


# In[18]:


df[df['BsmtCond'].isnull()]


# In[19]:


print(df['BsmtExposure'].isnull())


# In[20]:


df[df['BsmtExposure'].isnull()]


# In[35]:


df['BsmtExposure'].fillna('no exposure mentioned', inplace=True)


# In[22]:


df[df['BsmtExposure'].isnull()]


# In[23]:


print(df['BsmtFinType1'].isnull())


# In[24]:


df[df['BsmtFinType1'].isnull()]


# In[36]:


df['BsmtFinType1'].fillna('Values not mentioned', inplace=True)


# In[26]:


df[df['BsmtFinType1'].isnull()]


# In[27]:


print(df['BsmtFinType2'].isnull())


# In[28]:


df[df['BsmtFinType2'].isnull()]


# In[37]:


df['BsmtFinType2'].fillna('57', inplace=True)


# In[30]:


df[df['BsmtFinType2'].isnull()]


# In[31]:


print(df.isnull().sum())





