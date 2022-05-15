"""InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp"""


def insertion_sort(arr):
  index_length = range(1, len(arr))    
  for i in index_length:
    right = arr[i]
       
    while arr[i-1] > right and i>0:
      arr[i], arr[i-1] = arr[i-1], arr[i]
      i -= 1
    
  return arr


if __name__ == "__main__":
    new_list = [8, 4, 23, 42, 16, 15]
    print(insertion_sort(new_list))