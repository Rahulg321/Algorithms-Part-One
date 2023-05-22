s = "abc"

# def print_permutations(s):
#     perm_list = []
#     if len(s) == 1:
#         perm_list.append(s)
#         return 
#     else:
#         print_permutations(s[0:-1])

# print(s[0:-1])

def permutations(s):
    perm_list = [] 
    if len(s) == 1:
        perm_list.append(s)
        return s
    else:
        perm_list.append(s[0:-1])
        permutations(s[0:-1])
        print(perm_list)
       
permutations(s)


output_list = []

# insert x at every location

# for i in range(len(s) + 1):
#     string_list = list(s)
#     string_list.insert(i,"x")
#     word = "".join(string_list)
#     output_list.append(word)
    
# print(output_list)

# print_permutations(s, last_element=None)
    