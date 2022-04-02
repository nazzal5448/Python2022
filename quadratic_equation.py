def quadratic_Equation():
    import cmath
    a=float(input('Enter the value of a: '))
    b=float(input('Enter the value of b: '))
    c=float(input('Enter the value of c: '))

    step_1= (b**2) - 4*(a*c)
    step_2= cmath.sqrt(step_1)
    step_3 = -b+step_2
    step_4= -b-step_2

    print('The 1st value of x is :',step_3)
    print('The second value of x is :',step_4)

quadratic_Equation()