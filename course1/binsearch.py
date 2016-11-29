def binsearch(array, key, low, high):
    if high < low:
        return -1
    mid = int(low + (high - low) / 2)
    if key == array[mid]:
        return mid
    if key > array[mid]:
        return binsearch(array, key, mid + 1, high)
    if key < array[mid]:
        return binsearch(array, key, low, mid - 1)


arr = [1, 3, 5, 6, 7, 8]
print(binsearch(arr, 7, 0, len(arr) - 1))
