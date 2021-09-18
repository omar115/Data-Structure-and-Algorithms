def maxSum(arr, window_size):
    array_size = len(arr)
    if array_size <= window_size:
        print("Invalid Operation")
        return -1
    
    window_sum = sum(arr[i] for i in range(window_size))
    max_sum = window_sum

    # compute sum of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # current window

    for i in range(array_size - window_size):
        window_sum = window_sum - arr[i] + arr[i + window_size]
        max_sum = max(window_sum, max_sum)

    return max_sum



arr = [1, 2, 100, -1, 5]
answer = maxSum(arr, 3)
print(answer)