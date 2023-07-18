def generate_permutations(string):
    if len(string) <= 1:
        return [string]

    else:
        permutations = []
        for index, letter in enumerate(string):
            first_char = string[index]
            remaining_chars = string[0:index] + string[index + 1 :]

            print(f"first characters are {first_char}")
            print(f"remaining characters are {remaining_chars}")

            sub_permutations = generate_permutations(remaining_chars)

            print(f"sub permutations are {sub_permutations}")
            for sub_permutation in sub_permutations:
                permutation = first_char + sub_permutation
                permutations.append(permutation)
                print(f"permutations are {permutations}")

        return permutations


print(generate_permutations("abc"))
