"""
Given an array (or string), the task is to reverse the array/string.
"""

array = [1, 2, 3, 4, 5]
print(array)


def reverse_recursive(arr, first, last):
    if first > last:
        return
    arr[first], arr[last] = arr[last], arr[first]
    reverse_recursive(arr, first+1, last-1)


reverse_recursive(array, 0, len(array)-1)

print(array)
