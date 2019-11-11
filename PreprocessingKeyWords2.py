#!/usr/bin/env python
# coding: utf-8

# In[42]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import configparser
config = configparser.ConfigParser()
config.read('../config.ini')

import re
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
ps= PorterStemmer()
import spacy
nlp = spacy.load('en_core_web_sm')


import string
cachedStopWords = stopwords.words("english")


# In[40]:


class preprocessing():
    def __init__(self):
        return
    def removePunctuations(self,data):
            temp=re.sub(r'[^\w\s%]',' ',data.lower())            
            temp=re.sub(r'\s+',' ',temp)
            return temp
    
    def removeStopWords(self,data):
            words=word_tokenize(data)  
            words = [ps.stem(w) for w in words if not w in cachedStopWords]  
            return " ".join(words)
        
    def preprocess(self,text):
        processed_text=[]
        for i in text:
            #Remove punctuations
            #print(i)
            i=self.removePunctuations(i)
            tokens=self.removeStopWords(i)
            processed_text.append("".join(tokens))
        #print(processed_text)
        return processed_text
    
    def getSocialKeywords(self,text):
        processed_text=[]
        for sent in text:
            doc=nlp(sent)
            pos_text=""
            for token in doc:                 
                if((str(token.pos_) is not "VERB") and (str(token.pos_) is not "ADV") and (str(token.pos_) is not "ADP") and (str(token.pos_) is not "PUNCT")):
                    pos_text=pos_text+" "+str(token)
            
            processed_text.append(pos_text)
            
        #keywords=getSKeywords(processed_text)
        return processed_text
    
    def getAgencyKeywords(self,text):
            processed_text=[]
            for sent in text:
                doc=nlp(sent)
                pos_text=""
                for token in doc: 

                    if((str(token.pos_) is not "ADV") and (str(token.pos_) is not "ADP")):
                        pos_text=pos_text+" "+str(token)

                processed_text.append(pos_text)

            #keywords=getSKeywords(processed_text)
            return processed_text
        
    def parse_Resumefile(self,data,n):

        #This consists of ngram as key & count as value
        words=data.split(" ")

        #Prepare n-grams
        ngrams=self.ngrams(words,n)
        
        return list(ngrams)
    
    def build_ngram_distribution(self,data):
        n_s=[1,2,3] #uni, bi, and trigrams
        dist=[]
        for n in n_s:
            ngrams=self.parse_Resumefile(data,n)
            for i in ngrams:
                dist.append(" ".join(i))
        return dist
    
    
    #extracts all possible n-grams from the words stiched together
    def ngrams(self,input_list, n):
        return (zip(*[input_list[i:] for i in range(n)]))

    def getSocialNGrams(self,trainData):
        ngrams=[]
        trainData=self.preprocess(trainData)
        for row in trainData:
            ngrams.append(self.build_ngram_distribution(row))
        return ngrams




# In[46]:


# # # In[41]:

import pandas as pd
train_data=pd.read_csv("trainData.csv")
s=train_data['moment'].head(5)
#s=pd."But I am the real Strider, fortunately.I am Aragorn son of Arathorn; and if by life or death I can saved you, I will, I am real."
def main():
    p=preprocessing()
    #print(p.preprocess(s))
    #print(p.propernouns(s))
    #print(p.getSocialKeywords(s),"\n")
    print("\n\n\n",p.getSocialNGrams(s))
if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




