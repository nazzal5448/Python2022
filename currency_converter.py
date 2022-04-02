
while True:
    print('==================CURRENCY CONVERTER=================')
    print('''
        Which cuurency you want to convert your money from:
        1.INR
        2.PKR
        3.DOLLAR
        4.EURO
        5.YEN \n'''
        )
    a = int(input('Choose a number next to the currency: \n'))

    c= int(input('Enter the amount :\n'))

    if a ==1:
        print('''
        Which cuurency do you want to convert your money in:
        1.INR
        2.PKR
        3.DOLLAR
        4.EURO
        5.YEN \n'''
        )
        b=int(input('Choose the number next to the currency; \n'))

        if b==1:
            print(c*1,'INR')
        elif b==2:
            print(c*2.40 ,'PKR')
        elif b==3:
            print(c*0.013)
        elif b==4:
            print(c*0.012)
        elif b ==5:
            print(c*1.61)
        else:
            print('Invalid input')
    elif a==2:
        print('''
        Which cuurency do you want to convert your money in:
        1.INR
        2.PKR
        3.DOLLAR
        4.EURO
        5.YEN \n'''
        )
        b=int(input('Choose the number next to the currency; \n'))

        if b==1:
            print(c*0.42,'INR')
        elif b==2:
            print(c*1,'PKR')
        elif b==3:
            print(c*(1/185),'USD')
        elif b==4:
            print(c*0.0050,'EU')
        elif b ==5:
            print(c*0.67,"YEN")
        else:
            print('Invalid input')
    elif a==3:
        print('''
        Which cuurency do you want to convert your money in:
        1.INR
        2.PKR
        3.DOLLAR
        4.EURO
        5.YEN \n'''
        )
        b=int(input('Choose the number next to the currency; \n'))

        if b==1:
            print(c*75.74,'INR')
        elif b==2:
            print(c*185,'PKR')
        elif b==3:
            print(c*1,'USD')
        elif b==4:
            print(c*0.90,'EU')
        elif b ==5:
            print(c*121.93,'YEN')
        else:
            print('Invalid input')

    elif a==4:
        print('''
        Which cuurency do you want to convert your money in:
        1.INR
        2.PKR
        3.DOLLAR
        4.EURO
        5.YEN \n'''
        )
        b=int(input('Choose the number next to the currency; \n'))

        if b==1:
            print(c*84.16,'INR')
        elif b==2:
            print(c*202.15,'PKR')
        elif b==3:
            print(c*1.11,'USD')
        elif b==4:
            print(c*1,'EU')
        elif b ==5:
            print(c*135.42)
        else:
            print('Invalid input')

    elif a==5:
        print('''
        Which cuurency do you want to convert your money in:
        1.INR
        2.PKR
        3.DOLLAR
        4.EURO
        5.YEN \n'''
        )
        b=int(input('Choose the number next to the currency; \n'))

        if b==1:
            print(c*0.62,'INR')
        elif b==2:
            print(c*1.49,'PKR')
        elif b==3:
            print(c*0.0082,'USD')
        elif b==4:
            print(c*0.0074,'EU')
        elif b ==5:
            print(c*1,'YEN')
        else:
            print('Invalid input')

    else:
        print('Invalid input')

    d=int(input(
        '''
        Do you want to exit?
        1.yes
        2.No
        '''
    ))
    if d==1:
        break
    elif d==2:
        pass
    else:
        print('Invalid input')

print('Thanks for using our service.')
