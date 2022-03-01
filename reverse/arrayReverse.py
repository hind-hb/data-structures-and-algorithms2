def reverse_array(arr):
   
    revArr =[]
    lenArray=len(arr)
    while lenArray :
        revArr.append(arr[lenArray-1])
        lenArray-=1
    return revArr
    
print(reverse_array([1, 2, 3, 4, 5, 6]))
print(reverse_array([89, 2354, 3546, 23, 10, -923, 823, -12]))
print(reverse_array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]))