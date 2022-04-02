def mix_Number():
    a=int(input('Enter the number: '))
    while True:
        if a==1:
            print('''
                1 is neither prime nor composite.
                1 is odd.
                1 is a positive integer.
                ''')
            break

        elif a==2:
            print('''
                2 is prime, even and a positive integer.
                ''')
            break

        if (a%2)!=0:
            print(a,'is odd.')
        else:
            print(a,'is not odd.')

        if (a%2)==0:
            print(a,'is even number.')
        else:
            print(a,'is not even.')

        if a<0:
            print(a,'is negative integer.')
        else:
            print(a,'is positive integer.')

        if a>1 and a!=2:
            for i in range(2,a):
                if (a%i==0):
                    print(a,'is not prime')
                    break
                else:
                    print(a,'is prime.')
                    break
        break

mix_Number()