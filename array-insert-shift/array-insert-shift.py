import math


def insertShiftArray(arr, val):

    e = math.ceil(len(arr)/2)

    print(arr[:e] + [val] + arr[e:])

    return(arr[:e] + [val] + arr[e:])


insertShiftArray([1, 2, 3, 4, 5, 6], 15)