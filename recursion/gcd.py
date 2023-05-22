# find the greatest common divisor of two numbers using recursion
#(8,12) -> 4

def gcd(a, b):

    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print(gcd(48, 18))


def gcd2(a, b):
    assert int(a) == a and int(b) == b, "the numbers must be integers only"

    if a < 0:
        a = -1 * a

    if b < 0:
        b = -1 * b

    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print(gcd2(48, -1.8))
