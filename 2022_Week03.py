#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import pandas as pd


# In[14]:


df = pd.read_csv('data/PD 2022 Wk 1 Input - Input.csv')
df_grade = pd.read_csv('data/PD 2022 WK 3 Grades.csv')


# In[15]:


# Join the data sets together to give us the grades per student
df = df.merge(df_grade, how='left', left_on='id', right_on='Student ID')


# In[16]:


# Remove the parental data fields, they aren't needed for the challenge this week
df.drop(columns=['id', 'Parental Contact Name_1', 'Parental Contact Name_2',                 'Preferred Contact Employer', 'Parental Contact'],
       inplace=True)


# In[17]:


# Pivot the data to create one row of data per student and subject -> skip
# Rename the pivoted fields to Subject and Score -> skip


# In[18]:


# Create an average score per student based on all of their grades
# Round the average score per student to one decimal place
df["Student's Avg Score"] = (df['Maths'] + df['English'] + df['Spanish']                             + df['Science'] + df['Art'] + df['History'] + df['Geography']) / 7
df["Student's Avg Score"] = df["Student's Avg Score"].apply(lambda x : round(x, 1))


# In[32]:


# Create a field that records whether the student passed each subject -> skip
# Pass mark is 75 and above in all subjects
# Aggregate the data per student to count how many subjects each student passed
df['Passed Subjects'] = 0
subjects = [df['Maths'], df['English'], df['Spanish'], df['Science'], df['Art'], df['History'], df['Geography']]
for subject in subjects:
    df['Passed Subjects'] += subject.apply(lambda x: 1 if x >= 75 else 0)


# In[37]:


df.rename(columns={'gender':'Gender'}, inplace=True)


# In[41]:


# Remove any unnecessary fields and output the data
cols = ['Passed Subjects', "Student's Avg Score", 'Student ID', 'Gender']
df.to_csv('output-2022-week03.csv', index=False, columns=cols)


# In[43]:


df_output = pd.read_csv('output-2022-week03.csv')
df_output


# In[ ]:




