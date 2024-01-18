"""
Написати програму яка знаходить друге найменше число в списку.
1) з використанням методів списків, та вбудованих функцій
"""

def second_smallest1(array):
    unique_arr = list(set(array))
    unique_arr.sort()
    return unique_arr[1]

a = [1, 1, 2, 2, 3]
b = [-1, 10, -2, 2]
c = [1, -1, 2, 2, 3, -10, 10, -2, 2]

print(second_smallest1(a))
print(second_smallest1(b))

assert second_smallest1([1, 1, 2, 2, 3]) == 2
assert second_smallest1([-1, 10, -2, 2]) == -1

"""
2) без використання методів списків
"""

def second_smallest2(array):
    smallest = float('inf')
    second_smallest = float('inf')
    for i in array:
        if i < smallest:
            second_smallest = smallest
            smallest = i
        elif i < second_smallest and i != smallest:
            second_smallest = i
    return second_smallest

print(second_smallest2(a))
print(second_smallest2(b))
print(second_smallest2(c))

assert second_smallest2([1, 1, 2, 2, 3]) == 2
assert second_smallest2([-1, 10, -2, 2]) == -1
assert second_smallest2(c) == -2
