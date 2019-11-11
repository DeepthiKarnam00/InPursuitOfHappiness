#!/usr/bin/env python
# coding: utf-8

# In[21]:


from gensim.models import KeyedVectors
from gensim.models import Word2Vec
import numpy as np
from PreprocessingKeyWords import preprocessing
preprocessor=preprocessing()


# In[70]:


class Word2Vec2():
    
    
    def createWord2Vec(self):
        # Load vectors directly from the file
        model = KeyedVectors.load_word2vec_format('D:\\IIITH\\IR\\data\\GoogleNews-vectors-negative300.bin', binary=True)
        # Saving the model for later use. Can be loaded using Word2Vec.load()
        model.wv.save('Word2Vec_model.wv')
        #model.save('word2vec.model')
        
    def loadWord2Vec(self):
        #model = Word2Vec.load("word2vec.model")
        model=KeyedVectors.load("Word2Vec_model.wv", mmap='r')
        return model
    
    def getSentenceFeature(self,model,words):
        featureVec = np.zeros(300,dtype="float32")
        for word in words:
            if(word in model.vocab):
                featureVec=np.add(featureVec,model[word])
        
        featureVec=np.divide(featureVec,len(words))
        
        return featureVec
    
    def getSentenceFeature_Ngrams(self,model,ngramsList):
        featureVec = np.zeros(300,dtype="float32")
        tempVec= np.zeros(300,dtype="float32")
        for n in ngrams:
            words=n.split(" ")
            phrase=False
            featureVec=np.add(np.divide(tempVec,prevWordLen))
            tempVec=np.zeros(300,dtype="float32")
            for word in words:
                if(len(words)>1):
                    phrase=True
                    prevWordLen=len(words)
                if(word in model.vocab):
                    if(phrase is False):
                        featureVec=np.add(featureVec,model[word])
                    else:
                        tempVec=np.add(featureVec,model[word])
        
        featureVec=np.divide(featureVec,len(ngramsList))
        
        return featureVec
    
    def getFeatureMatrix(self, model,trainData):
        trainSize=len(trainData)
        featureMatrix = np.zeros((trainSize,300),dtype="float32")
        
        for i,row in enumerate(trainData):
            tokens=row.split(" ")
            featureMatrix[i]=self.getSentenceFeature(model,tokens)
        
        return featureMatrix
    
    def getFeatureMatrix_Ngrams(self, model,trainData):
        trainSize=len(trainData)
        featureMatrix = np.zeros((trainSize,300),dtype="float32")
        
        for i,row in enumerate(trainData):
                featureMatrix[i]=self.getSentenceFeature(model,row)
        
        return featureMatrix
            
        
        


# In[71]:


a=Word2Vec2()


# In[72]:


# a.createWord2Vec()


# In[73]:


b=a.loadWord2Vec()


# In[76]:


import pandas as pd
train_data=pd.read_csv("trainData.csv")
data=train_data['moment']
print(a.getFeatureMatrix_Ngrams(b,data))
print("\n\n\n\n",a.getFeatureMatrix(b,data))


# In[ ]:




