"""
№3 Створити програму, яка перестворює список із вкладеними списками на звичайний.
вхідні [['Vlad', 'Kira'], ['Dima', 'Dasha', ['Nikita']], 'Vova']
вихідні ['Vlad', 'Kira', 'Dima', 'Dasha', 'Nikita', 'Vova']
"""

def flatten_list(nested_list):
    flattened_list = []

    for sublist in nested_list:
        if isinstance(sublist, list):
            flattened_list.extend(flatten_list(sublist))
        else:
            flattened_list.append(sublist)

    return flattened_list

names1 = ["Adam",["Bob", ["Chet","Cat"], "Barb", "Bert"],"Alex",["Bea","Bill"],"Ann"]
names2 = [['Vlad', 'Kira'], ['Dima', 'Dasha', ['Nikita']], 'Vova']
assert flatten_list(names1) == ["Adam","Bob","Chet","Cat","Barb","Bert","Alex","Bea","Bill","Ann"]
assert flatten_list(names2) == ['Vlad', 'Kira', 'Dima', 'Dasha', 'Nikita', 'Vova']
assert flatten_list([]) == []
assert flatten_list([[], "Hello", [1, 2, [], 3], "World"]) == ["Hello", 1, 2, 3, "World"]
