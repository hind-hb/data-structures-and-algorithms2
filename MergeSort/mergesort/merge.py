"""ALGORITHM Mergesort(list)
    DECLARE n <-- list.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- list[0...mid]
      DECLARE right <-- list[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, list)

ALGORITHM Merge(left, right, list)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            list[k] <-- left[i]
            i <-- i + 1
        else
            list[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in list to remaining values in right
    else
       set remaining entries in list to remaining values in left
"""


def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)
        merge(arr,left,right)
    return arr


def merge(arr,left,right):
  i = 0
  j = 0
  k = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      arr[k] = left[i]
      i+=1
    else:
      arr[k] = right[j]
      j+=1
    k+=1
 
  while i < len(left):
    arr[k] = left[i]
    i+=1
    k+=1

  while j < len(right):
    arr[k] = right[j]
    j+=1
    k+=1