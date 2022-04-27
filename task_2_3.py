class BankAccount:
    def __init__(self,accountNumber, name, balance):
        self.acno= int(accountNumber)
        self.name=name
        self.balance= int(balance)

    def deposit(self,amount):
        print(amount, 'is deposited. Your new balance is',self.balance + amount)

    def withdraw(self, amount):
        print(amount, 'is withdrawn. Your new balance is ', self.balance-amount)

    def bankFees(self):
        print('The current fee on your balance is ',self.balance*0.05)

    def display(self):
        print('Following are your account details:')
        print('Name :', self.name)
        print('Account Number:', self.acno)
        print('Balance:' , self.balance)


account= BankAccount(908909, 'Nazzal Kausar', 80000)
account.display()
# account.withdraw(6000)
account.deposit(8000)
account.bankFees()


