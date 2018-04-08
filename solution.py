
# coding: utf-8

# In[27]:


import pandas as pd
import string
import re

data = pd.read_csv("test.csv", sep=',')

def clean_text(text):
    text = "".join([word for word in text if word not in string.punctuation])
    tokens = re.split('\W+', text)
    text = [word for word in tokens if word not in stopwords]
    return text

stopwords = nltk.corpus.stopwords.words('english')
data['question1tokens'] = data['question1'].apply(lambda x: clean_text(str(x).lower()))
data['question2tokens'] = data['question2'].apply(lambda x: clean_text(str(x).lower()))
data.head()


# In[23]:


import nltk

wn = nltk.WordNetLemmatizer()


# In[28]:


def lemmatizing(tokenized_text):
    text = [wn.lemmatize(word) for word in tokenized_text]
    return text

data['question1lemmatized'] = data['question1tokens'].apply(lambda x: lemmatizing(x))
data['question2lemmatized'] = data['question2tokens'].apply(lambda x: lemmatizing(x))

data.head()


# In[29]:


def countProba(l1,l2):
    same = int(0)
    for tokn in l1:
        if tokn in l2:
            same+=1
    pro = same/(len(l1)+len(l2)-same+1)
    return pro

list1 = []
for l1 in data['question1lemmatized']:
    list1.append(l1)

list2 = []
for l1 in data['question2lemmatized']:
    list2.append(l1)

len(list1)


# In[30]:


import csv

with open("outout_quora.csv",'w',newline='') as file:
    writer = csv.writer(file,delimiter=',')
    writer.writerow(['test_id','probability'])
    #fileData['question_id'],fileData['']
    for i in range(len(list1)):
        writer.writerow([i,countProba(list1[i],list2[i])])
        #print([i,countProba(list1[i],list2[i])])
print('Done')

