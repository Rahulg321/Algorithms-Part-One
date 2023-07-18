hash_table = {}

n = 3


def find_solution_pairs(n, hash_table):
    for a in range(n + 1):
        for b in range(n + 1):
            result = (a**3) + (b**3)
            hash_table[result] = (a, b)

    print(hash_table)
    for pair in hash_table.values():
        print(pair)


find_solution_pairs(n, hash_table)
