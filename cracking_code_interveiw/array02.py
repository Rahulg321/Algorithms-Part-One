"""
    given two sorted arrays find the number of elements in common
"""


def binary_search(arr):
    pass

def common_elements(arr1, arr2):
    common_elements_index = 0
    hash_table = {}
    for element in arr1:
        hash_table[element] = element

    for element in arr2:
        if element in hash_table.keys():
            print(f"common element->", element)
            common_elements_index += 1

    return common_elements_index


arr1 = [13, 27, 35, 40, 49, 55, 59]
arr2 = [17, 35, 39, 40, 55, 58, 60]

print(common_elements(arr1, arr2))
