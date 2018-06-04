# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 11:16:18 2016

@author: apple
"""
from statistics import median
import mmh3, re
#result estimations from all hash functions
result=[0]*663
#read each line in the file
with open('tweetstream.txt') as f:
    for line in f:
        #loop in all hashtags        
        if re.findall('text":.*","source',line):
            hashtags=re.findall('#([^ \t\n\r\f\v,"]*)',re.findall('text":.*","source',line)[0])
            if hashtags:
                                
                for hashtag in hashtags:
                    for i in range(663):
                        #hash the hashtag in to [u]    
                        hashvalue=mmh3.hash(hashtag, i) % 576308
                        #find number of trailing 0
                        trailing_zeros=len(bin(hashvalue))-len(bin(hashvalue).rstrip('0'))
                        #always keep maxium value to each hash function                        
                        result[i]=trailing_zeros if trailing_zeros>result[i] else result[i]
# find the median among all results
print (median(result))
