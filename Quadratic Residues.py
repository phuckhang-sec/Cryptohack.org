"""
p=29 
ints=[14,6,11]
Find x that a^2 ≡ x mod p / x in ints
"""
p = 29
ints = [14, 6, 11]
for a in range(29):
    x = pow(a, 2, p)
    if x in ints:
        print("a = ", a, " then x = ", x)