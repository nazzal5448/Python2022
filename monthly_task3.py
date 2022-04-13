print('=================Task 3==============')

def lqueue():
    s=[]
    a1=0
    while a1<5:
       #FIFO 
        print('''What Do You want to Do?
            1- add to Queue
            2- remove from Queue
            3- length of the Queue
            4- check If it's empty
            ''')
        a=int(input('Choose a number: '))
        a1+=1
        if a==1:
            add=input('enter the value to add: ')
            s.append(add)
        elif a==2:
            if len(s)>0:
                s.pop(0)
                print(s)
            else:
                print('Queue is empty.')
        elif a==3:
            print(len(s))
        elif a==4:
            if len(s) ==0:
                print('queue is empty')
            else:
                print('queue is not empty')

lqueue()