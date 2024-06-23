#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = {"Name": ["John", "Peter", "Lisa"],
       "Age": [25,28,31],
       "Salary": [300000,45000,25000]}

df = pd.DataFrame(data)
print(df)


# In[4]:


# in case of csv file
data = pd.read_csv("C:/Users/DELL/Downloads/company.csv")
print(data)


# In[12]:


# in case of excel file
data = pd.read_excel("C:/Users/DELL/Downloads/expense3.xlsx")
print(data)


# In[13]:


# Exploring data in pandas

import pandas as pd
data = pd.read_excel("C:/Users/DELL/Downloads/ESD.xlsx")
print(data)
print(data.head(10))
print(data.tail(10))


# In[14]:


print(data.info())


# In[15]:


data.describe()


# In[18]:


print(data.isnull().sum())


# In[20]:


# Handling duplicate values in pandas

import pandas as pd

data = pd.read_csv("C:/Users/DELL/Downloads/company1.csv")
print(data)


# In[22]:


print(data["EEID"].duplicated().sum())


# In[23]:


print(data.drop_duplicates("EEID"))


# In[3]:


# Working with missing data in pandas 

import pandas as pd

data = pd.read_csv("C:/Users/DELL/Downloads/company1.csv")
print(data)



# In[33]:


print(data.isnull().sum())


# In[27]:


print(data.dropna())


# In[28]:


print(data)


# In[29]:


import numpy as np

print(data.replace(np.nan,30000))


# In[37]:


data["salary"] = data["salary"].replace(np.nan, 24400)
print(data)
print(data["salary"].mean())


# In[35]:


print(data["salary"].mean())


# In[4]:


print(data)


# In[5]:


print(data.fillna(method = "bfill"))


# In[6]:


print(data.fillna(method = "ffill"))


# In[7]:


print(data.fillna("hii"))


# In[9]:


# columns transformation in pandas

import pandas as pd

df = pd.read_excel("C:/Users/DELL/Downloads/ESD.xlsx")
# print(df)

df.loc[(df["Bonus %"] == 0, "GetBonus")] = "no bonus"
df.loc[(df["Bonus %"] > 0, "GetBonus")] = "bonus"
print(df.head(10))


# In[2]:


import pandas as pd

data = pd.read_excel("C:/Users/DELL/Downloads/ESD.xlsx")
print(data.head(10))


# In[16]:


gp = data.groupby(["Department","Gender"]).agg({"EEID":"count"})
print(gp)


# In[17]:


gp1 = data.groupby("Country").agg({"Annual Salary": "mean"})
print(gp1)


# In[3]:


gp1 = data.groupby(["Country","Gender"]).agg({"Annual Salary": "max","Age": "min"})
print(gp1)


# In[5]:


# Merge, join ,concatenate in pandas

import pandas as pd

data1 = {"Emp Id": ["E01","E02","E03","E04","E05","E06"],
        "Names":["Ram","Shyam","Rahul","Vishal","Ravi","John"],
        "Age": [34,56,23,44,32,36]}

data2 = {"Emp Id": ["E01","E02","E03","E04","E05","E06"],
        "Salary": [45000,56000,34000,30000,50000,62000]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(df1)
print()
print(df2)


# In[7]:


# merge 

print(pd.merge(df1,df2, on = "Emp Id"))


# In[8]:


import pandas as pd

data1 = {"Emp Id": ["E01","E02","E03","E04","E05","E06"],
        "Names":["Ram","Shyam","Rahul","Vishal","Ravi","John"],
        "Age": [34,56,23,44,32,36]}

data2 = {"Emp Id": ["E01","E07","E03","E04","E08","E06"],
        "Salary": [45000,56000,34000,30000,50000,62000]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(df1)
print()
print(df2)


# In[10]:


print(pd.merge(left = df1, right = df2, on = "Emp Id" , how = "left"))


# In[11]:


print(pd.merge(left = df1, right = df2, on = "Emp Id" , how = "right"))


# In[15]:


# concatenate

import pandas as pd

data1 = {"Emp Id": ["E01","E02","E03","E04","E05","E06"],
        "Names":["Ram","Shyam","Rahul","Vishal","Ravi","John"],
        "Age": [34,56,23,44,32,36]}

data2 = {"Emp Id": ["E07","E08","E09","E010","E011","E012"],
       "Names":["bittu","chintu","pappu","chotu","bunty","golu"],
        "Age": [34,56,23,44,32,36]}


df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)


# In[17]:


print(pd.concat([df1,df2]))


# In[18]:


# compare DataFrames in pandas

import pandas as pd

dict = {"Fruites": ["mango", "apple","banana","papaya"],
       "Price": [100,150,50,35],
       "Quantity": [15,10,10,3]}

df1 = pd.DataFrame(dict)
print(df1)


# In[22]:


df2 = df1.copy()

df2.loc[0,"Price"] = 120
df2.loc[1,"Price"] = 175
df2.loc[2,"Price"] = 30
df2.loc[0,"Quantity"] = 12
df2.loc[1,"Quantity"] = 15
df2.loc[2,"Quantity"] = 5

print(df2)
print(df1.compare(df2,align_axis = 0))


# In[24]:


print(df1.compare(df2))
print(df1.compare(df2,keep_equal = True))


# In[25]:


print(df1.compare(df2))
print(df1.compare(df2,keep_shape = True))


# In[26]:


print(df1.compare(df2))
print(df1.compare(df2,keep_shape = False))


# In[27]:


# pivoting and melting dataframes 

dict = {"Keys": ["k1","k2","k1","k2"],
        "Names": ["John","Ben","David","Peter"],
        "Houses": ["red","blue","green","red"]}

df = pd.DataFrame(dict)
print(df)
print(df.pivot("Keys","Names","Houses"))
        
        


# In[29]:


dict = {"Keys": ["k1","k2","k1","k2"],
        "Names": ["John","Ben","David","Peter"],
        "Houses": ["red","blue","green","red"],
       "Grades": ["3rd","8th","9th", "8th"]}

df = pd.DataFrame(dict)
print(df)
print(df.pivot(index="Keys",columns="Names",values=["Houses","Grades"]))


# In[34]:


# melting

dict = {"Names": ["John","Ben","David","Peter"],
        "Houses": ["red","blue","green","red"],
       "Grades": ["3rd","8th","9th", "8th"]}

df = pd.DataFrame(dict)
print(df)
print(pd.melt(df, id_vars=["Names"],value_vars=["Houses","Grades"]))
print(pd.melt(df, id_vars=["Names"],value_vars=["Houses","Grades"],var_name="Houses&Grades", value_name="values"))

