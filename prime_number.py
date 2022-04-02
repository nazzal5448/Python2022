def prime():    
    a=int(input('Enter the number:\n'))
    if a>1:
        for i in range(2,a):
            if (a%i==0):
                print(a,'is not prime')
                break
            else:
                print(a,'is prime.')
                break
    else:
        if a==1:
            print('1 is neither prime nor composite.')
        else:
            print('Invalid entry')

prime()