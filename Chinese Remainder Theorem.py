"""
x ≡ 2 mod 5
x ≡ 3 mod 11
x ≡ 5 mod 17
Find the integer a such that x ≡ a mod 935
"""
def extended(u, v):
    """Extended Euclidean Algorithm to find x and y such that gcd(u, v) = x*u + y*v"""
    if v == 0:
        return u, 1, 0
    else:
        gcd, x1, y1 = extended(v, u % v)
        x = y1
        y = x1 - (u // v) * y1
        return gcd, x, y

def invert(a, m):
    """Modular inverse using Extended Euclidean Algorithm"""
    gcd, x, _ = extended(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    else:
        return (x % m + m) % m

def chinese_remainder_theorem(a, m):
    """Solve the system of linear congruences using the Chinese Remainder Theorem"""
    mk = 1
    for mi in m:
        mk *= mi

    x = 0
    for ai, mi in zip(a, m):
        Mi = mk // mi
        yi = invert(Mi, mi)
        x += ai * Mi * yi

    return x

a = [2, 3, 5]
m = [5, 11, 17]

result = chinese_remainder_theorem(a, m)
print(result % 935)
