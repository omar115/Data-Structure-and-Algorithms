
def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while (left <= right):
        
        mid = (left + right) // 2    # 0...5 => (0+5)//2 = 2
        
        # note: the double forward slash is known as integer division operator.
        # it will keep the whole number component of a result, i.e. 5 // 2 => 2.5 but // will
        # keep the value 2 only.

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            # 0 1 2 m=3 4 5 t=6, so, t > m and left = 3+1 = 4
            left = mid + 1
        else:
            right = mid - 1
    
    return -1



arr = [1,2,3,4,5,6]
target = 6

result = binarySearch(arr, target)

if result != -1:
    print("Element is present at index number ", result)

else:
    print("Element is not present in the array")