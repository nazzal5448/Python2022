def bmi():
    print('This is BMI calculator in Metric units.')
    w= float(input('Enter your wight in Kg: '))
    h= float(input('Enter your height in meters: '))
    bm= w/(h**2)
    print('Your body mass index is:',bm)

bmi()