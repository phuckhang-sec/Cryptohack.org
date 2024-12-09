"""
Using the two primes p = 26513, q = 32321, find the integers u, v such that:
                p.u + q.v = gcd(p,q)
"""

def extended(p, q):
    if q == 0:
        return p, 1, 0
    else:
        gcd, u1 , v1 = extended(q, p%q)
        u = v1
        v = u1 - v1* (p//q) 
        return gcd, u, v

p = 26513
q = 32321
print(extended(p,q))




