"""
Your task is to compute the total number of comparisons used to sort the given input file by QuickSort.  As you know, the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three different pivoting rules.

1.For the first part of the programming assignment, you should always use the first element of the array as the pivot element.

2.Compute the number of comparisons (as in Problem 1), always using the final element of the given array as the pivot element.  Again, be sure to implement the Partition subroutine exactly as it is described in the video lectures.
Recall from the lectures that, just before the main Partition subroutine, you should exchange the pivot element (i.e., the last element) with the first element.

3.Compute the number of comparisons (as in Problem 1), using the "median-of-three" pivot rule.  [The primary motivation behind this rule is to do a little bit of extra work to get much better performance on input arrays that are nearly sorted or reverse sorted.]  In more detail, you should choose the pivot as follows.  Consider the first, middle, and final elements of the given array.  (If the array has odd length it should be clear what the "middle" element is; for an array with even length 2k2k, use the k^{th}k 
th
  element as the "middle" element. So for the array 4 5 6 7,  the "middle" element is the second one ---- 5 and not 6!)  Identify which of these three elements is the median (i.e., the one whose value is in between the other two), and use this as your pivot.  As discussed in the first and second parts of this programming assignment, be sure to implement Partition exactly as described in the video lectures (including exchanging the pivot element with the first element just before the main Partition subroutine).

EXAMPLE: For the input array 8 2 4 5 7 1 you would consider the first (8), middle (4), and last (1) elements; since 4 is the median of the set {1,4,8}, you would use 4 as your pivot element.
"""

res = 0
def sub_sort(array,low,high):
    i = low
    j = low+1
    # problem1 do nothing

    # problem2 
    # array[high], array[low] = array[low], array[high]

    # problem3
    mid = (high + low) // 2
    if mid_of3(array[mid], array[low], array[high]):
        array[mid], array[low] = array[low], array[mid]
    elif mid_of3(array[high], array[low], array[mid]):
        array[high], array[low] = array[low], array[high]
    else:
        pass

    while j <= high:
        if array[j] >= array[low]:
            j += 1
        else:
            i += 1
            array[i], array[j] = array[j], array[i]
            j += 1
    array[low] ,array[i] = array[i], array[low]
    return i

def quick_sort(array,low,high):
    global res 
    if low < high:
        res += high - low
        key_index = sub_sort(array,low,high)
        quick_sort(array,low,key_index-1)
        quick_sort(array,key_index+1,high)

def mid_of3(a,b,c):
    return (a < b and a > c) or (a > b and a < c)

if __name__ == '__main__':
    with open('test.txt') as f:
        a = f.readlines()

    nums = [int(i.strip()) for i in a]
    print(nums)
    quick_sort(nums, 0, len(nums)-1)
    print(nums)
    print(res)


    # 162085
    # 164123
    # 138382
