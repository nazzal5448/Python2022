
def deposit():
    total= 5000
    a= int(input('Enter the amount to deposit: '))
    total+=a
    print('Amount deposited successfully!')
    print('Your remaining balance is',total)

def withdraw():
    total= 5000
    a= int(input('Enter the amount to withdraw: '))
    total-=a
    print('Amount withdrawn successfully!')
    print('Your remaining balance is:', total)

def exit():
    print('Atm exited succesfully!')

def check_Balance():
       print('Your total balance is: 5000')

while True:
    print('Welcome to HBL atm. Choose an option: 1,2,3 \n')
    choice = input('1. Check balance 2. Withdraw amount 3. Deposit amount \n ')
    if int(choice)==1:
        check_Balance()
    elif int(choice)== 2 :
        withdraw()
    elif choice==3:
        deposit()
    else:
        print('Invalid choice')

    ex= input ('''
                 Do you want to exit?
                 1.yes
                 2.no
                 ''')
    if int(ex)==1:
        exit()
        break
    elif int(ex)==2:
        pass
    else:
        print('invalid input')