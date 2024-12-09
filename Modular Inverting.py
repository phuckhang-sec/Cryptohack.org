"""
3.d ≡ 1 mod 13
Find d?
"""
def extended(a, m):
    if m == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended(m, a%m)
        x = y1
        y = x1 - y1*a//m
        return gcd, x, y
    
def invert(a, m):
    gcd, x, _ = extended(a, m)
    if gcd != 1:
        print("The value of d is not exsist")
    else:
        return (x % m + m) % m #The result is a positive number.

a = 3
m = 13
d = invert(a, m)
print(d)