"""
11≡x mod 6 
8146798528947≡y mod 17 
The solution is the smaller of the two integers (x,y)
"""
x = 11 % 6
y = 8146798528947 % 17
if (x>y):
    print(x)
else: 
    print(y)