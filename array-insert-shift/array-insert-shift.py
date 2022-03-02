def insertShiftArray(arr,val):
    Arrnew=[]
    arr1=arr[:int(len(arr)/2)]
    arr2=arr[int(len(arr)/2):]
    arr1.append(val)
    Arrnew=arr1+arr2  
    return Arrnew  
if __name__ == "__main__":
    print(insertShiftArray([2, 4, 6, 8], 5))
    print(insertShiftArray([42,8,15,23,42], 16))
