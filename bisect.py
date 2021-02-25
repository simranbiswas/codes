#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    r=0
    l=len(expenditure)
    arr= expenditure[l-d-1:l-1]
    arr.sort()
    mid=math.floor(d/2)
    e=d%2
    i=l-1
    while i>=d:
        if e ==0 :
            m=float((arr[mid]+arr[mid-1])/2)
        else :
            m=arr[mid]
        if expenditure[i]>=2*m:
            r=r+1
        del arr[bisect.bisect_left(arr,expenditure[i-1])]
        bisect.insort(arr, expenditure[i-d-1])
        i=i-1
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
