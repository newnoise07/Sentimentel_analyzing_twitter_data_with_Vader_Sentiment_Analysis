# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 01:39:22 2020

@author: hp
"""

import matplotlib.pyplot as plt
import numpy as np

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
neg_count = 0
neg_correct = 0
pos_count = 0
pos_correct = 0

with open("Betikİng.txt","r") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if not vs['neg'] > 0.1:
            if vs['pos']-vs['neg'] > 0:
                pos_correct += 1
            pos_count +=1
        
with open("Betikİng.txt","r") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if not vs['pos'] > 0.1:
            if vs['pos']-vs['neg'] <= 0:
                neg_correct += 1
            neg_count +=1
toplam = pos_count+neg_count;
print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))
print(toplam)
values = [neg_correct,pos_correct]
plt.figure(figsize=(12,6))
y = [52.12,86.51]
x_labels = ['Pozitif','Negatif']
x_pos = np.arange(len(y))
plt.bar(x_pos,y,color=['green','blue'],
       linewidth = 5,
       width = [0.1,0.1])
plt.bar(x_pos,y)
plt.title("Tweet Sayısı İle Duygu Durumu Oranı")
plt.xticks(x_pos,x_labels);
plt.xlabel("Duygu Durumu")
plt.ylabel("Tweet Yüzdesi")
plt.show();





