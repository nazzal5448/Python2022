def gci():
    print('=====================Gross Commission Income Calculator==================')
    sp=int(input('Enter the sale price: '))
    cp=int(input('Enter the commission percentage: '))
    income= sp*(cp/100)
    print('Your Gross Commission Income is:',income)

gci()
