# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:40:13 2019

@author: Srn
"""

#########################################
#####      quickSort      1         ##### 
#########################################
def quickSort(arr, left, right):
    # 递归终止条件
    if left > right:
        return
    
    i = left
    j = right
    pivot = arr[left]
    
    while i < j:
        print(arr, i, j, pivot)
       
        while i < j and arr[j] >= pivot:
            j -= 1
        while i < j and arr[i] <= pivot:
            i += 1 
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        
    # 将选择的中心点放置于合适的位置
    arr[left] = arr[i]
    arr[i] = pivot
    
    quickSort(arr, left, i-1)
    quickSort(arr, i+1, right)
    
arr = [-1, 3, 0, 9, 10, 0]
quickSort(arr, 0, len(arr)-1)
print('quickSort:',arr)

#########################################
#####      quickSort   2            ##### 
#########################################
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    
    small = [x for x in arr if x < pivot]
    great = [x for x in arr if x > pivot]
    mid = [x for x in arr if x == pivot]
    return quickSort(small) + mid + quickSort(great)


#########################################
#####      insertSort               ##### 
#########################################
def insertSort(arr):
    length = len(arr)
    for i in range(length):
        k = i
        for j in range(k,0,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
    return arr

arr = [-1, 3, 0, 9, 10, 0]
insertSort(arr)
print('insertSort:',arr)


#########################################
#####      shellSort               ##### 
#########################################
def shellSort(arr):
    step = len(arr) // 2
    
    while step > 0:
        for i in range(step, len(arr)):
            while i >= step and arr[i] < arr[i-step]:
                arr[i], arr[i-step] = arr[i-step], arr[i]
                i -= step
        step //= 2
    
    return arr

arr = [-1, 3, 0, 9, 10, 0]
shellSort(arr)
print('shellSort:',arr)



#########################################
#####      heapSort               ##### 
#########################################
def buildMaxHeap(arr):
    import math
    for i in range(math.floor(len(arr)/2),-1,-1):
        heapify(arr,i)

def heapify(arr, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)
        arrLen -=1
        heapify(arr, 0)
    return arr

arr = [-1, 3, 0, 9, 10, 0]
heapSort(arr)
print('heapSort:',arr)


#########################################
#####      heapSort               ##### 
#########################################
class HeapSort:
    def heapSort(self, arr):
        length = len(arr)
        if length <= 1:
            return arr
        else:
            for i in range(length, 0, -1):
                firstNum = self.adjustHeap(arr, i)
                arr[i-1], arr[0] = firstNum, arr[i-1]
        
        return arr
    
    
    def adjustHeap(self, arr, length):
        
        i = length //2 - 1
        
        # fisrt index is 0
        while i >= 0:
            left = i * 2 + 1
            right = i * 2 +2
            
            #large = arr[i]  # get parent node as large value
            
            # if left child node exist
            while left < length:
                
                # get large between left and right
                if right < length and arr[left] < arr[right]:
                    left = right
                
                # get large between children and parent nodes
                if arr[left] > arr[i]:
                    arr[left], arr[i] = arr[i], arr[left]
                    # new i
                    i = left
                else:
                    break
                
                # new left and right
                left = 2 * left + 1
                right = left + 1
            
            i -= 1
        
        return arr[0]
                
arr = [-1, 3, 0, 9, 10, 0, 2, 0, 7, -2, 40, 32]
s = HeapSort()
arr = s.heapSort(arr)
print('heapSort:',arr)               

        

#########################################
#####      mergeSort               ##### 
#########################################
def mergeSort(arr):
    if len(arr) <= 1:
        return arr  # 递归终止条件
    
    mid = len(arr) // 2
    
    # 分
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    
    # 治
    return merge(left, right)

def merge(left, right):
    i,j = 0,0
    result = []  # 额外的空间消耗
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
    if i < len(left):
        result += left[i:]
    if j < len(right):
        result += right[j:]
    
    return result

arr = [-1, 3, 0, 9, 10, 0, 2, 0, 7, -2, 40, 32]
s = mergeSort(arr)
print('mergeSort:',s) 


def countingSort(arr):
    
    if len(arr) <= 1:
        return arr
    
    max_arr = max(arr)
    min_arr = min(arr)
    
    count_len = max_arr - min_arr + 1
    count_arr = [0] * count_len
    
    result = [0] * len(arr)
    
    for i in arr:
        count_arr[i - min_arr ] += 1
    
    for j in range(1,count_len):
        count_arr[j] += count_arr[j-1] 
    
    # 倒排写入结果，得到稳定排序结果
    for k in arr[::-1]:
        result[count_arr[k-min_arr] - 1] = k
        count_arr[k] -= 1
    
    return result
        
arr = [-1, 3, 0, 9, 10, 0, 2, 0, 7, -2, 40, 32]
s = countingSort(arr)
print('countingSort:',s)

