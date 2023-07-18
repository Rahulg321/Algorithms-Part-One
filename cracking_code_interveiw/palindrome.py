"""
    given a string find the longest paldinromic substring
"""


def isPalidromePointer(str):
    left = 0
    right = len(str) - 1
    result = True

    while left < right:
        if str[left] != str[right]:
            result = False
            break

        left += 1
        right -= 1

    return result



def isPalindrome(str):
    if len(str) <= 1:
        return True

    if str[0] == str[-1]:
        return isPalindrome(str[1:-1])


# print(isPalidromePointer("mom"))

# print(isPalindrome("moms"))


def print_str(str):
    for length in range(len(str), 0, -1):
        for start in range(len(str) - length + 1):
            print(str[start : start + length])


print_str("abcde")


print("i am not sure how i want to go about implementing it")


