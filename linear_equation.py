def linear_Equation():
    print('This program will solve equation of the form ax+b = 0')
    a= int(input('Enter the value of a: '))
    b= int(input('Enter the value of b: '))
    if a>0:
        x= -b/a
        print('The value of x is:',x)
    else:
        print('invalid input')

linear_Equation()
