s = "   -42"


def myAtoi(s):
    length = len(s)
    is_negative = False
    number_str = ""
    i = 0
    operator_checked = False
    
    while i < length and s[i] == " ":
        i += 1
    
   
    
    
    
    while i < length and s[i].isdigit():
        
        if s[i] == "-" or s[i] == "+":
            if s[i] == "-":
                is_negative = True
                
        if s[i] == "-" or s[i] == "+":
            return 0
        
        number_str += s[i]
        i += 1
    
    
    if not number_str:
        return  0
    
    if is_negative:
        number_str = "-" + number_str

    # print(number_str)
    
    if number_str:
        result = int(number_str)
        if is_in_32bit_signed_range(result) == True:
            print("yes it is outside range")
            result = clamp_to_32bit_signed_range(result)
            print(f'clamped result is {result}')
        return result
    else:
        return 0


def is_in_32bit_signed_range(number):
    if number < -2147483648:
        return True
    elif number > 2147483647:
        return False


def clamp_to_32bit_signed_range(number):
    if number < -2147483648:
        return -2147483648
    elif number > 2147483647:
        return 2147483647
    else:
        return number


print(myAtoi(s))
