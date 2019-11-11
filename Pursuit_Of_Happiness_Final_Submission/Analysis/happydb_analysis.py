#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sklearn import preprocessing
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


df = pd.read_csv("dataset.csv") 


# In[5]:


df.head()


# In[6]:


df.columns


# In[7]:


df.shape


# ### **Data Analysis**
# 

# In[ ]:


#Removing id 
t_df = df.drop(df.columns[[0,1,2,6,11]], axis=1)       #Removing hmid,happymoment,concepts,country,duration


# In[10]:


t_df.head()


# In[11]:


t_df.shape


# In[12]:


#Encoding categorical labels
label_encoder = preprocessing.LabelEncoder()
cols = [0,1,3,4,5,6]          #not for age
for i in cols:
    print(t_df.columns[i])
    label_encoder.fit(t_df.iloc[:,i].astype('str'))
    print(list(label_encoder.classes_))
    t_df.iloc[:,i] = label_encoder.transform(t_df.iloc[:,i].astype('str')).astype('float64')
    


# In[ ]:


df_agency = t_df[['agency','age','gender','married','parenthood','reflection']]
df_social = t_df[['social','age','gender','married','parenthood','reflection']]


# # Correlation among Features

# ### Agency

# In[15]:


corr1 = df_agency.corr()
corr1


# In[16]:


f,ax = plt.subplots(figsize=(7,6))
sns.heatmap(corr1)
plt.title("Correlation of features for Agency",y=1.05)


# Social

# In[17]:


corr2 = df_social.corr()
corr2


# In[18]:


f,ax = plt.subplots(figsize=(7,6))
sns.heatmap(corr2)
plt.title("Correlation of features for Social",y=1.05)


# ## Length of moments

# In[ ]:


moments_a = df[['moment','agency']]
moments_s = df[['moment','social']]


# In[ ]:


def len_moment(moment):
    moment = moment.strip()
    moment = moment.split()
    return len(moment)


# Agency

# In[21]:


yes_length = 0
yes_count = 0
no_length = 0
no_count = 0

for i in range(len(moments_a)):
    moment = moments_a.iloc[i][0]
    agency = moments_a.iloc[i][1]
    if( agency == "yes"):
        yes_count += 1
        yes_length += len_moment(moment)
    else:
        no_count += 1
        no_length += len_moment(moment)
    
    
print("Avg length of moment for Agency-YES : ",(float(yes_length)/float(yes_count)))
print("Avg length of moment for Agency-NO : ",(float(no_length)/float(no_count)))


# Social

# In[22]:


yes_length = 0
yes_count = 0
no_length = 0
no_count = 0

for i in range(len(moments_s)):
    moment = moments_s.iloc[i][0]
    social = moments_s.iloc[i][1]
    if( social == "yes"):
        yes_count += 1
        yes_length += len_moment(moment)
    else:
        no_count += 1
        no_length += len_moment(moment)
    
    
print("Avg length of moment for Social-YES : ",(float(yes_length)/float(yes_count)))
print("Avg length of moment for Social-NO : ",(float(no_length)/float(no_count)))

