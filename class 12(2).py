print("==============Task 2(2)=============== \n")
while True:
	print("\n Do you want to use atm machine? \n")
	user=input("Yes/No \n")
	if user=="no":
		break
	else:
		pass
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
print('\nThanks for using our services♡')	