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




