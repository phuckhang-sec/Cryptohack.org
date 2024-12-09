"""
caculate gcd(a, b) with a = 66528, b = 52920

"""

def gcd(a, b):
    if b == 1:
        return a
    else:
        return gcd(b, b%a)
    
a = 66528
b = 52920 
print(gcd(a, b))