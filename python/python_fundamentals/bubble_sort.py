# bubble sort video in Python fundamentals (evaluates and swaps two values at a time)

def bubbleSort(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-1-j):  # -j because you don't have to start from the beginning (index zero) in the second iteration
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
print(bubbleSort([1,5,3,2,0,8]))