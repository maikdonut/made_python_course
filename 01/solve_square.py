from math import isclose

def quad_eq(a,b,c):
    if isclose(a, 0):
        return "Not quadratic equation"
    d = b**2 - 4*a*c
    if (d<0):
        return "No real roots"
    elif (isclose(d, 0)):
        return -b/(2*a)
    return ((-b + d**0.5)/(2*a), (-b - d**0.5)/(2*a))
        
assert quad_eq(5, 1, 2) == "No real roots"
assert quad_eq(1, 5, 6) == (-2, -3)
assert quad_eq(4, -4, 1) == 0.5
assert quad_eq(1, 9.75, -2.5) == (0.25, -10)
assert quad_eq(0, 1, 1) == "Not quadratic equation"

a = float(input('Enter a:'))  
b = float(input('Enter b:'))  
c = float(input('Enter c:'))
quad_eq(a,b,c)
