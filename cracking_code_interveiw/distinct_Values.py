"""
    find pairs with difference k = 2
"""

test_array = [1, 7, 5, 9, 12, 3]


def find_pairs(arr, k):
    hash_table = {}
    for element in arr:
        hash_table[element] = element

    result = 0

    for element in hash_table:
        result = k + element

        if result in hash_table:
            print("Pair =>", result, element)


find_pairs(test_array, 2)
