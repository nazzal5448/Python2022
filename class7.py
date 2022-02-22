print('================Task 1==================')

num1=int(input('Enter the first number: '))
num2=int(input('Enter the second number: '))
print(num1,' + ' ,num2 ,' = ' , num1+num2)
print(num1,' - ' ,num2 ,' = ' , num1-num2)
print(num1,' X ' ,num2 ,' = ' , num1*num2)
print(num1,' / ' ,num2 ,' = ' , num1/num2)
print(num1,' // ' ,num2 ,' = ' , num1//num2)
print(num1,' % ' ,num2 ,' = ' , num1%num2)

print('================Task 2==================')

a1=input('Enter the first value: ')
a2 = input('Enter the second value: ')
print(a1==a2)

print('================Task 3==================')

len=int(input('Enter the length of the plot in meters: '))
wid= int(input('Enter the width of the plot in meters: '))
print('The area of the plot is: ' , len*wid ,' square meters')

print('================Task 4 (a)==================')
weight= float(input('Please enter your age in Kg: '))
height= float(input('Please enter your height in cm: '))
print('Your body mass index is: ', weight/(height**2))

print('================Task 4 (b)==================')
w1 = float(input('Enter your weight in pounds: '))
h1 = float(input('Enter your height in inches: '))
print('Your body mass index is: ' , (w1/(h1**2))*703)

print('================Task 5 (1)==================')
print('your weight in pounds = ' , weight*2.205)
print ('Your height in inches = ' , height*39.37)

print('================Task 5 (2)==================')
radian= float(input('Enter the value in radian: '))
print('Your value in degrees = ' , radian*57.296)

print('================Task 6 (1)==================')

print('==========AREA OF TRAPEZOID============')
b1 = int(input('Enter the length of base 1: '))
b2 = int(input('Enter the length of base 2: '))
h = int(input('Enter the height of trapezoid: '))
print('The area of the given trapezoid = ',((b1+b2)/2)*h)

print('================Task 6 (2)==================')
print('===========AREA OF PARRALLELOGRAM=============')
base = int(input('Enter the length of base: '))
h2 = int(input('Enter the height of parrallelogram: '))
print('The area of the given parrallelogram = ', base*h2)

print('================Task 6 (3)==================')
print('============AREA  AND VOLUME OF CYLINDER==============')

radius= int(input('Enter the radius of cylinder: '))
hc= int(input('Enter the height of the cylinder: '))
print('Surface area of cylinder = ', 2*3.14*(radius+hc))
print('Volume of cylinder = ', 3.14*(radius**2)*hc)

print ('Any suggestion for improvement of the program would be highly appreciated :)')
