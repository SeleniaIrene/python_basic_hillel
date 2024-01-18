"""
написати програму, яка приймає два списки та видає новий список зі спільними унікальними елементами
"""

def list_intercection(list1, list2):
    common_elements = []
    for i in list1:
        if i in list2 and i not in common_elements:
            common_elements.append(i)
    if not common_elements:
        return None
    return common_elements

assert list_intercection([1, 1, 1, 2], [1, 3, 4]) == [1, ]
assert list_intercection(["foo", 1, "bar"], [2, 3, 4]) == None
assert list_intercection(["foo", 1, "bar"], []) == None
assert list_intercection(["foo", 1, "bar"], [4, "foo", 7]) == ["foo", ]
