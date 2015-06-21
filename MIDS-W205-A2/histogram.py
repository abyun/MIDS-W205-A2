#W205.3 - Al Byun
#Assignment 2
#3. Analyze the acquired tweets by producing a histogram (a graph) of the words.

import nltk
import os
import sys
from nltk.tokenize import RegexpTokenizer

# Change default encoding to prevent any UnicodeEncodeErrors
reload(sys)
sys.setdefaultencoding("utf-8")

# read in text files with tweets and tokenize the words
tokens = []
tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
for file in os.listdir("C:\\Users\\Albert\\desktop\\github\\Assignment2\\"):
    if file.endswith(".txt"):
        tweet_file = open(file,'r')
        tweet_file.readline()
        for line in tweet_file:
            tokens = tokens + tokenizer.tokenize(line)
        tweet_file.closed

#remove stopwords
stopWords = nltk.corpus.stopwords.words('english')
stopWords = stopWords + ['.',',','http','rt','?','!',':','!!!','https','!!',"'s","'t",'...','\xf0','\x9f\x99\x88','"','\x80\xa6','\xe2','\xc2']
#convert tokens to lowercase
tokens_lower_filtered = [e.lower() for e in tokens if not e.lower() in stopWords]

# build a frequency distribution
fdist1 = nltk.FreqDist(tokens_lower_filtered) 
top_30 = fdist1.most_common(30)
#fdist1.plot(30, cumulative=True) #this was not working due to a UnicodeDecodeError 

# plot histogram
words =[]
counts =[]
for word,count in top_30:
    words.append(str(word))
    counts.append(int(count))


# plot the histogram
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

# also create a CSV file of the words and counts for ease of analysis
top_30_new = zip(words,counts)
top_30_df= pd.DataFrame(data = top_30_new, columns=['words','counts'])
top_30_df.to_csv('tweet_freq_Warriors.csv')

# create the histogram plot
indexes = np.arange(len(words))
plt.bar(indexes, counts)
plt.xticks(indexes, words, rotation=30)
plt.xlabel('Most Frequent Words')
plt.ylabel('Frequency')
plt.title('Histogram of Most Frequent Words in Tweets Containing #Warriors (7-14 June 2015)')
plt.show()