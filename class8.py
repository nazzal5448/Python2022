print('=============Task 1============')
current_balance  = 5000
print('Welcome to HBL atm. Choose an option: 1,2,3 \n')
choice = input('1. Check balance 2. Withdraw amount 3. Deposit amount \n ')
if int(choice)==1:
    print('Your current balance is: ' , current_balance)
elif int(choice)== 2 :
    wa= input('Enter the amount you want to withdraw: \n')
    if int(wa)>current_balance:
        print('Insufficient balance')
    else:
        print('Amount withdrawn successfully!')
elif choice==3:
    dep = int(input('Enter the amount you want to deposit: \n'))
    current_balance += dep
    print ('Amount Deposited successfully!')
    print('Your new balance is: ', current_balance)
else:
    print('Invalid choice')
    
print ('=================Task 2==================')

exp=int(input('Tell us your years of experience in numbers: \n'))
if exp<4:
    print('You are selected for management. ')
else:
    print('You are shortlisted as a developer.')
    
print('================Task 3===========')
interests=input('Tell me about your field of interests: \n')
if interests=='bio':
    
    print('I suggest you better go for some medical fields. They match your interests')
elif interests=='humanity':
    print('I suggest you better go for some medical fields. They match your interests')
elif interests=='science':
    print('I suggest you better go for some medical fields. They match your interests')
elif interests=='discipline':
    print('I suggest you better go for some medical fields. They match your interests')
    
elif interests== 'drawing':
    print('You better pursue your career in arts domain.')
elif interests=='arts':
    print('You better pursue your career in arts domain.')
elif interests=='writing':
    print('You better pursue your career in arts domain.')
elif interests =='management':
    print('You better pursue your career in arts domain.')
elif interests=='computer':
    print('You Will do better in Engineering fields.')
elif interests=='technology':
    print('You Will do better in Engineering fields.')
elif interests=='problem solving':
    print('You Will do better in Engineering fields.')
elif interests=='programming':
    print('You Will do better in Engineering fields.')
    
else:
    print('I need more information.')
    
    
    
