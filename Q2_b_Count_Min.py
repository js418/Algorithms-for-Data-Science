# 590D Algorithm for Data Science
# Jie Song, Buqin Wang, Swetal Bhatt
# Homework 2
# Question 2_b

import re
import time
import mmh3
import numpy
from MinHeap import *

e = 0.001 # error parameter
w = 2718 # array size
d = 31 # number of hash functions
m = 581932 # total number of twitters with hashtag


def main():

    start = time.time()

    matrix = numpy.zeros((d,w)) # initialize the T table with 0s
    heap = MinHeap()

    f = open( "tweetstream.txt", "r" )
    for line in f:
        subs = re.findall('"text":.*","source"',line)
        if subs:            
            hashtag = re.findall('#([^ \t\n\r\f\v,"]*)',subs[0])
            if hashtag:
                for i in range(len(hashtag)):
                    counter = [0]*d
                    # count-min sketch
                    for j in range(d):
                        key = mmh3.hash(hashtag[i], j) % (w+1)
                        matrix[j][key-1] += 1
                        counter[j] = matrix[j][key-1]   #store d hash values for each item in a list
                    min_value = int(min(counter))
                    # if the counter of coming item is above m/k, insert it to the min-heap
                    if min_value >= int(m*0.001):
                        heap.replace_item(hashtag[i],min_value)
                        if not heap.replace_item(hashtag[i],min_value):
                            heap.insert(hashtag[i],min_value)

    f.close

    heavy_hitters = heap.get_list()
    print 'The list of hashtags that occur at least 0.001th fraction of times is:'
    print heavy_hitters
    print 'It has', len(heavy_hitters), 'hashtags returned'

    heavy_hitters2 = []
    for data in heavy_hitters:
        if data[1] >= int(m*0.002):
            heavy_hitters2.append(data)
    print 'The list of hashtags that occur at least 0.002th fraction of times is:'
    print heavy_hitters2
    print 'It has', len(heavy_hitters2), 'hashtags returned'
    
    stop = time.time()
    print 'running time is', stop - start, 'seconds'

main()
