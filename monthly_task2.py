print('=============Task 2==============')

def stack():
    s=[]
    a1=0
    while a1<5:
        #LIFO
        print('''What Do You want to Do?
        1- add to stack
        2- remove from stack
        3- length of the stack
        4- check If it's empty
        ''')
        a=int(input('Choose a number: '))
        a1+=1
        if a==1:
            add=input('enter the value to add: ')
            s.append(add)
        elif a==2:
            s.pop()
        elif a==3:
            print(len(s))
        elif a==4:
            if len(s) ==0:
                print('stack is empty')
            else:
                print('stack is not empty')
stack()