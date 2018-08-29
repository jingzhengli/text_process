# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 09:26:55 2018

@author: lenovo
"""

'''
===========================================
  @author:  jiaxin         
  @time:    2018/7/22 0022   21:08 
===========================================
'''
#print('输入范例：')
#n = int(input())
#m = int(input())
#n_shape = input()
#map = []
#for i in range(n):
#    line = [int(x) for x in input().split()]
#    map.append(list(line))
n, m = 3, 2
map = [[0, 2, 3], [2, 0, 1], [3, 1, 0]]
# n, m = 4, 3
# map = [[0, 2, 4, 3], [2, 0, 5, 3], [4, 5, 0, 4], [3, 3, 4, 0]]
    
    
    
    
res = [([float('inf')]*n)for _ in range(n)]
 
 
def mypath(n, m, distance):
    if m == 0:
        if res[source][n] > distance:
            res[source][n] = distance
            return
        return
    info = map[n]
    for i, j in enumerate(info):
        if j != 0:
            mypath(i, m-1, distance + j)
    return
 
 
for i in range(n):
    source = i
    mypath(i, m, 0)
 
print('输出范例：')
for i in res:
    print(i)
