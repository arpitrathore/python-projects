"""
Given an array (or string), the task is to reverse the array/string.
"""

array = [1, 2, 3, 4, 5]
print(array)


def reverse_normal(arr, first, last):
    while(first < last):
        arr[first], arr[last] = arr[last], arr[last]
        first += 1
        last -= 1


reverse_normal(array, 0, len(array)-1)

print(array)
