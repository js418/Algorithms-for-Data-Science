# 590D Algorithm for Data Science
# Jie Song, Buqin Wang, Swetal Bhatt
# Coding Assignment 1
# Question 2
# K-means++ algorithm


import time
import random
import math
from math import factorial

K = 5

def distance(x,y):
    d = 0
    for i in range(13):
        d += pow(x[i]-y[i],2)
    return d

def center_(a):
    c = []
    n = len(a)
    for i in range(13):
        b = 0
        for j in range(n):
            b += a[j][i]
        c.append(round(b/n,2))
    return c 

def com(n, r):
    if n < r:
        return 0
    else:
        return factorial(n) // factorial(r) // factorial(n-r)

def main():
    
    start = time.time()

    print 'Given K =', K

    # store all the datas as points in a list
    f = open('wine.data.txt','r')
    points = []
    for line in f:
        data = line.strip().split(',')
        del data[0]
        for i in range(13):
            data[i] = float(data[i])
        points.append(data)
    f.close
    N = len(points)

    # randomly pick the first center from all points
    c_new = []
    c = random.randint(0,N-1)
    c_new.append(points[c])

    # pick other K-1 centers 
    for i in range(1,K):
        dis = []
        dis_p = []
        # compute the the distance between each point and its closest center
        for j in range(N):
            d = distance(points[j],c_new[0])
            for m in range(len(c_new)):
                if distance(points[j],c_new[m])<d:
                    d = distance(points[j],c_new[m])
            dis.append(d)
        # random generate a value r in [0,1]
        r = random.random()
        dis_sum = sum(dis)
        # calculate the probability distribution
        for x in range(N):
            dis_p.append(dis[x]/dis_sum)
        # find the point where that r value falls, which is the new center
        index = min(range(N), key=lambda i: abs(dis_p[i]-r))
        c_new.append(points[index])

    
    # Recompute the new cluster centers by K-means
    while True:
        c_old = c_new
        clusters = [ [] for k in range(K)]
        c_id = [ [] for k in range(K)]
        for i in range(N):
            d = distance(points[i], c_old[0])
            label = 0
            for j in range(K):
                if distance(points[i],c_old[j]) < d:
                    d = distance(points[i],c_old[j])
                    label = j
            clusters[label].append(points[i])
            c_id[label].append(i)
        for k in range(K):
            c_new[k] = center_(clusters[k])
        if c_old == c_new:
            break

    print 'The centers of', K,'clusters by K-means++ are:', c_new

    #print 'The clusters are:'
    for i in range(K):
        print 'Cluster', i, 'with', len(clusters[i]), 'points in it'
        #print clusters[i]

    g_id = [ list(i for i in range(59)),list(j for j in range(59,130)),list(k for k in range(130,178))]

    c_in = [ [] for k in range(K)]
    pos_agree = 0
    for i in range(K):
        for j in range(3):
            inter = set(c_id[i]).intersection(g_id[j])
            c_in[i].append(len(inter))
            pos_agree += com(c_in[i][j],2)
    print c_in
    neg_agree = 0
    for i in range(K-1):
        for j in range(i+1,K):
            neg_agree += c_in[i][0]*c_in[j][1] + c_in[i][0]*c_in[j][2]
            neg_agree += c_in[i][1]*c_in[j][0] + c_in[i][0]*c_in[j][2]
            neg_agree += c_in[i][2]*c_in[j][0] + c_in[i][0]*c_in[j][1]

    total_agree = pos_agree + neg_agree
    print 'The total agreement is:', total_agree   

    stop = time.time()

    print 'running time is', stop - start, 'seconds'
    
main()
