# a should be greater than b
def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b,a%b)


a = 66528 
b = 52920
print(gcd(a,b))

