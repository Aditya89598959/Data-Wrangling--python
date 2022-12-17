#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import pandas as pd #Pandas is a high-level data manipulation tool
import numpy as np #NumPy is used for working with multidimensional arrays


# In[2]:


print(pd.show_versions())


# # Load the 1st  dataset

# In[3]:


dataset_1=pd.read_csv('rental_bike_descr.csv')


# # Observations
# * We have to upload the dataset in the file explorer on the left panel of your lab
# * We are reading the file through the dataset_1 variable
# * The file is in CSV format
# * We use the pd.read_csv() function to read a CSV file
# * We provide the exact path of the file within the round bracket ()
# 

# # Check the type of dataset

# In[4]:


type(dataset_1)


# # Observations:
# * The result shows that the dataset is DataFrame
# * DataFrame is a tabular structure consisting of rows and columns
# 

# In[5]:


dataset_1.shape


# # Observation:
# * The dataset_1 has 610 rows and 10 columns

# # Print first 5 rows of the dataset

# In[6]:


dataset_1.head()


# # Observation:
# * The 'dataset_1.head()' function displays only the initial five rows of the dataset.

# # Load the 2nd data
# * use the function carefully since it is an excel file

# In[7]:


dataset_2= pd.read_excel ('rental_bike_season .xlsx')


# In[8]:


# Shape of the dataset
dataset_2.shape


# # Observation:
# * The result shows that dataset_2 has 610 rows and 8 columns.
# 

# In[9]:


# Print first 5 rows of the dataset
dataset_2.head()


# # Observation:
# * We can see a column named unnamed:0 , which is not in the data dictionary. Let's remove it.
# 

# # Drop the column

# In[10]:


dataset_2=dataset_2.drop(['Unnamed: 0'],axis=1)


# In[11]:


# dLets check the shape of the dataset again after the drop
dataset_2.shape


# In[12]:


#Let's check the dataset_2 again
dataset_2.head()


# # Observation:
# * dataset_2 does not have Unnamed: 0 column

# # Merge the datasets
# * We have two datasets. They are dataset_1 and dataset_2
# * As both datasets have one common column 'instant', let's merge the datasets on that column
# 
# * We are going to save the resultant data inside the combined_data as shown below
# 

# In[13]:


combined_data=pd.merge(dataset_1,dataset_2, on='instant')


# In[14]:


combined_data.shape


# In[15]:


combined_data.head()


# # Now, load the 3rd dataset
# * The dataset is saved in s3 bucket, we are going to download the dataset_3

# In[16]:


dataset_3=pd.read_csv('final_rental_bike_dataset.csv')


# In[17]:


dataset_3.shape


# In[18]:


dataset_3.head()


# In[19]:


# Bottom rows of the dataset
dataset_3.tail()


# In[20]:


#Bottom 15 rows of the dataset
dataset_3.tail(15)


# # Sort values of a column
# * To sort the values per our will, we use the sort_values function and in the square brackets, we specify the name of the column by  which we want to sort, as shown below
# 
# 

# In[21]:


dataset_3=dataset_3.sort_values(by=['instant'])


# In[22]:


dataset_3


# In[23]:


dataset_3.head()


# In[24]:


dataset_3.tail()


# # Concatenate the combine_data with dataset_3
# * Let's concatenate both DataFrame combined_data and dataset_3 into a single DataFrame using the concat function, as shown below
# * Store the final DataFrame inside the final_data variable

# In[25]:


final_data=pd.concat([combined_data,dataset_3])


# In[26]:


final_data.shape


# # Let's diplay the columns of the final_data DataFrame

# In[27]:


final_data = final_data.rename(columns={'dteday': 'date', 'yr': 'year', 'mnth':'month','hr':'hour', 'weathersit':'weather', 'hum':'humidity', 'cnt':'count'})


# In[28]:


final_data.head()


# # Data types of different column values

# In[29]:


final_data.dtypes


# # Observations:
# We can see that the majority of our data columns are of type int64. They are therefore 64-bit integers. Some of the columns are of the
# type float64, which implies that they have decimals in them. However, only the date column has an object type, indicating that it
# contains strings.
# Check for null values
# Execute the given command to check the unknown values in the DataFrame

# In[30]:


final_data.isnull()


# # Drop the rows with missing values
# we will use the dropna function to drop the null value rows
# 

# In[31]:


final_data = final_data.dropna(axis=0)
final_data.shape


# In[32]:


final_data.isna().sum(axis=0)


# # Perform sanity checks on the dataset
# It verifies the logical correctness of the data points

# # Check if casual + registered is always equal to count

# In[33]:


np.sum(final_data['casual'] + final_data['registered'] - final_data['count'])


# # Month values should be in the range of 1-12
# We will use the unique() function to find the elements of an array

# In[34]:


np.unique (final_data.month)


# # Hour should be in the range of 1-24

# In[35]:


np.unique(final_data.hour)


# # Print the statistical summary of the data
# We will use the describe() function to see the stastical summary of the dataset

# In[36]:


print(final_data.describe())


# 

# In[ ]:




