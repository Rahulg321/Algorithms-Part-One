def generate_string_permutations(s, current_permutation, result):
    if len(current_permutation) == len(s):
        result.append(''.join(current_permutation))
        return

    for char in s:
        if char not in current_permutation:
            current_permutation.append(char)
            generate_string_permutations(s, current_permutation, result)
            current_permutation.pop()

input_string = "ab"
result = []
generate_string_permutations(input_string, [], result)

for perm in result:
    print(perm)

    