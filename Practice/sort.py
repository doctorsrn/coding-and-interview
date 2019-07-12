# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 14:50:36 2019

@author: Srn
"""

from functools import wraps
import wrapt

def log(func):
    @wraps(func)
    def with_log(*args, **kwargs):
        print(func.__name__ + " was called:")
        print(func(*args, **kwargs))
        return func(*args, **kwargs)
    return with_log

@wrapt.decorator
def logit(wrapped, instance, args, kwargs):
    print(wrapped.__name__ + " was called:")
    print(wrapped(*args, **kwargs))
    return wrapped(*args, **kwargs)

@logit
def bubbleSort(arr):
    if len(arr) <= 1:
        return arr
    
    length = len(arr)
    
    for i in range(length-1):
        for j in range(i+1,length):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            
    return arr

arr = [2,7,9,-2,4,5,2,10,0]
bubbleSort(arr)


@logit
def selectSort(arr):
    if len(arr) <= 1:
        return arr
    
    length = len(arr)
    
    for i in range(length-1):
        m = i+1
        for j in range(i+1,length):
            if arr[m] < arr[j]:
                m = j
        
        if arr[m] > arr[i]:
            arr[i], arr[m] = arr[m], arr[i]
    
    return arr

arr = [2,7,9,-2,4,5,2,10,0]
selectSort(arr)


@logit
def insertSort(arr):
    if len(arr) <= 1:
        return arr
    
    length = len(arr)
    
    for i in range(1,length):
        current = arr[i]
        j = i-1
        while(j >= 0 and arr[j] < current):
           
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current
            
    return arr

arr = [2,7,9,-2,4,5,2,10,0]
insertSort(arr)

@logit
def shellSort(arr):
    if len(arr) <= 1:
        return arr
    
    length = len(arr)
    step = length // 2
    while step > 0:
        for i in range(step, length):
            while i >= step and arr[i-step] < arr[i]:
                arr[i-step], arr[i] = arr[i], arr[i-step]
                i -= 1
        step //= 2
    
    return arr

arr = [2,7,9,-2,4,5,2,10,0]
shellSort(arr)
        

# 解决递归函数的装饰器会多次打印的问题，在嵌套一个函数就可以
@logit
def quickSort(arr):
    def _quickSort(arr):
        if len(arr) <= 1:
            return arr
        
        length = len(arr)
        pivot = arr[length // 2]
        
        
        left = [x for x in arr if x > pivot]
        right = [x for x in arr if x < pivot]
        mid = [x for x in arr if x == pivot]
        
        return _quickSort(left)+mid+_quickSort(right)
    return _quickSort(arr)

arr = [2,7,9,-2,4,5,2,10,0]
quickSort(arr)


@logit
def mergeSort(arr):
    def _mergeSort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        
        left = _mergeSort(arr[0:mid])
        right = _mergeSort(arr[mid:len(arr)])
        
        return merge(left, right)
    return _mergeSort(arr)

def merge(left, right):
    
    l = 0
    r = 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(right[r])
            r += 1
        else:
            result.append(left[l])
            l += 1
    
    if l == len(left):
        result += right[r:len(right)]
    if r == len(right):
        result += left[l:len(left)]
    
    return result
    
arr = [2,7,9,-2,4,5,2,10,0]
mergeSort(arr)  
    

@logit
def heapSort(arr):
    if len(arr) <= 1:
        return arr
    
    length = len(arr)
    for i in range(length-1):
        m = adjustHeap(arr, length-i)
        arr[0], arr[length-i-1] = arr[length-i-1], m
        
    return arr
    

def adjustHeap(arr, length):
#    print(arr)
    if length <= 1:
        return arr

    # 非叶子节点
    pa = length // 2 - 1
    
    # 小顶堆
    while pa >= 0:
        left = pa * 2 + 1
        right = pa * 2 + 2
        m = left 
        
        while left < length:
            if right < length and arr[left] > arr[right]:
                m = right
            
            if arr[m] < arr[pa]:
                arr[pa], arr[m] = arr[m], arr[pa]
            else:
                break

            left = m * 2 + 1
            right = m * 2 + 2
            m = left
        
        pa -= 1
    
    return arr[0]

arr = [2,7,9,-2,4,5,2,10,0]
heapSort(arr)


@logit
def countingSort(arr):
    if len(arr) <= 1:
        return arr
    
    mi = min(arr)
    ma = max(arr)
    
    count = [0] * (ma-mi+1)
    result = [0] * len(arr)
    
    for i in arr:
        count[i-mi] += 1
    
    for j in range(1,len(count)):
        count[j] += count[j-1]
    
    # 反向写入
    for k in arr[::-1]:
        result[count[k-mi]-1] = k
        count[k-mi] -= 1
    
    return result

arr = [2,7,9,-2,4,5,2,10,0]
countingSort(arr)


#@logit
# 针对均匀分布在[0,1]之间的数的桶排序
class bucketSort(object):
    def insertSort(self,a):
        n=len(a)
        if n<=1:
            pass
        for i in range(1,n):
            key=a[i]
            j=i-1
            while key<a[j] and j>=0:
                a[j+1]=a[j]
                j-=1
            a[j+1]=key
    
    @logit
    def bucketsort(self,a):
        n=len(a)
        s=[[] for i in range(n)]
        for i in a:
            s[int(i*n)].append(i)
        for i in s:
            self.insertSort(i)
        return [i for j in s for i in j]
    def __call__(self,a):
        return self.bucketsort(a)

arr = [0.2,0.3,0.5,0.12,0.46]
a = bucketSort()
a.bucketsort(arr)


# 基数排序，典型的整数排序算法
@logit
def radixSort(s):
    if len(arr) <= 1:
        return arr
    i = 0 # 记录当前正在排哪一位，最低位为1
    max_num = max(s)  # 最大值
    j = len(str(max_num))  # 记录最大值的位数
    while i < j:
        bucket_list =[[] for _ in range(10)] #初始化桶数组
        for x in s:
            bucket_list[int(x / (10**i)) % 10].append(x) # 找到位置放入桶数组
        # print(bucket_list)
        s.clear()
        for x in bucket_list:   # 放回原序列
            for y in x:
                s.append(y)
        i += 1
    return s

s = [334,5,67,345,7,345345,99,4,23,78,45,1,3453,23424]   
radixSort(s)





