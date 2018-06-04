# 590D Algorithm for Data Science
# Jie Song, Buqin Wang, Swetal Bhatt
# Homework 1
# Question 4

import re
re.compile('<title>(.*)</title>')
import random
import string
import math

u = 20000000 # assumed number of tweets
k = 443 # number of hash functions

#generate the hash function
def hash(string_,a,b):
    key = 0
    for i in range(0, len(string_)-1):
        key += ord(string_[i])*pow(10,len(string_)-1-i)
    index = ((a*key + b)% 15485863)%20000000
    return index

def main():

    z_max = 0
    a=[0]*k
    b=[0]*k
    for i in range (0,k):
        a[i] = random.randint(1,15485863)
        b[i] = random.randint(1,15485863)

    f = open( "tweetstream.txt", "r" )
    for line in f:
        
        subs = re.findall('"text":.*","source"',line)
        '''
        the hashtags appeared in the "text" field of tweet data,
        which is before "source" field
        '''
        if subs !=[]:            
            hashtag = re.findall('#([^ \t\n\r\f\v,"]*)',subs[0])
            '''
             for a hashtag, if it appears in the middle of a tweet,
             it will be followed by a space;
             if it appears at the end of the tweet,
             it will be followed by ","source"
            '''
            if hashtag != []:
                #print (subs)
                print (hashtag)
                #print ()

                for i in range(0,len(hashtag)):
                    for j in range(0,k):
                        key = hash(hashtag[i],a[j],b[j])
                        bin_key = bin(key)
                        if key == 0:
                            z = 0
                        else:
                            z = len(str(bin_key))- str(bin_key).rindex('1')-1
                        if z > z_max:
                            z_max = z
                
                
    f.close

    estimate_value = pow(2,z_max)
    print ('The estimate distinct has tags in the stream is', estimate_value)


main()
