def quad_eq(a,b,c):
    assert a != 0, 'Not quadratic equation'
    d = b**2 - 4*a*c
    if (d<0):
        print("No real roots")
    elif (d==0):
        print(f'Root is:{-b/(2*a)}')
    else:
        print(f'First root is:{(-b + d**0.5)/(2*a)}')
        print(f'Second root is:{(-b - d**0.5)/(2*a)}')

a = float(input('Enter a:'))  
b = float(input('Enter b:'))  
c = float(input('Enter c:'))
quad_eq(a,b,c)
