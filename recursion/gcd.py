def gcd(a, b):
    if a ==  0:
        return b
    elif b == 0:
        return a 
    else:
        g = a % b
        return gcd(b, g)
    
print(gcd(100, 75))