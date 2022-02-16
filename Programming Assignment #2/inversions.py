"""
This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.

 Your task is to compute the number of inversions in the file given, where the i^{th}i 
th
  row of the file indicates the i^{th}i 
th
  entry of an array.

  Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.

The numeric answer for the given input file should be typed in the space below.

So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any other punctuation marks. You can make up to 5 attempts, and we'll use the best one for grading.

(We do not require you to submit your code, so feel free to use any programming language you want --- just type the final numeric answer in the following space.)

[TIP: before submitting, first test the correctness of your program on some small test files or your own devising.  Then post your best test cases to the discussion forums to help your fellow students!]
"""

counts = 0

def mergeSort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    a = mergeSort(array[:mid])
    b = mergeSort(array[mid:])
    return merge(a,b)

def merge(array1, array2):
    global counts 
    res = []
    m = len(array1)
    n = len(array2)
    i,j = 0,0
    while i < m and j < n:
        if array1[i] <= array2[j]:
            res.append(array1[i])
            i += 1
        else:
            res.append(array2[j])
            counts += m-i
            j += 1
        
    while i < m:
        res.append(array1[i])
        i += 1
    while j < n:
        res.append(array2[j])
        j += 1
    return res


def reversePairs(nums):
    if len(nums) <= 1: return 0
    if len(nums) == 2: return 1 if nums[0] > nums[1] else 0
    more,less=[],[]
    count=0
    centercount=0
    center=nums[len(nums)//2]
    for i in nums:
        if i>center:
            more.append(i)
        elif i==center:
            centercount+=1
            count+=len(more)
        else:
            count+=centercount
            count+=len(more)
            less.append(i)
    count+=reversePairs(more)+reversePairs(less)
    return count

if __name__ == '__main__':
    with open('IntegerArray.txt') as f:
        array = [int(i.strip()) for i in f.readlines()]
    mergeSort(array)
    print(counts)
    print(reversePairs(array))