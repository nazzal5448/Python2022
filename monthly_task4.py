print('=================Task 4================')

books= 200
names=['c','python','java','blogging','seo','wordpress','html','computer','web','php']
python =20
java = 20
c=20
web=20
wordpress=20
computer=20
php=20
html=20
blogging=20
seo =20
while True:
    
    def sell():
        print('''Here is the list of the books. Choose one:
            1- C#
            2- Python
            3- Computer science
            4- Java
            5- Php
            6- Html
            7- web development
            8- WordPress
            9- Blogging
            10- Seo''')
        a= int(input('Choose the number next to the book: '))
        if a==1:
            global c
            if c >0:
                print('Book is sold')
                c-=1
            else:
                print('Book is not present. You need to restock.')
        elif a==2:
            global python
            if python >0:
                print('Book is sold')
                python-=1
            else:
                print('Book is not present. You need to restock.')
        elif a==3:
            global computer
            if computer >0:
                print('Book is sold')
                computer-=1
            else:
                print('Book is not present. You need to restock.')
        elif a==4:
            global java
            if java >0:
                print('Book is sold')
                java-=1
            else:
                print('Book is not present. You need to restock.')
             
        elif a==5:
            global php
            if php >0:
                print('Book is sold')
                php-=1
            else:
                print('Book is not present. You need to restock.')
        elif a==6:
            global html
            if html >0:
                print('Book is sold')
                html-=1
            else:
                print('Book is not present. You need to restock.')
        elif a==7:
            global web
            if web >0:
                print('Book is sold')
                web-=1
            else:
                print('Book is not present. You need to restock.')
        elif a==8:
            global wordpress
            if wordpress >0:
                print('Book is sold')
                wordpress-=1
            else:
                print('Book is not present. You need to restock.')
        elif a==9:
            global Blogging
            if blogging >0:
                print('Book is sold')
                blogging-=1
            else:
                print('Book is not present. You need to restock.')
        elif a==10:
            global seo
            if seo >0:
                print('Book is sold')
                seo-=1
            else:
                print('Book is not present. You need to restock.')
        else:
            print('invalid choice')
    def restock():
        names=['c','python','java','blogging','seo','wordpress','html','computer','web','php']
        name= input('Enter the name of the book: ')
        q=int(input('Enter the quantity: '))
        for book in names:
            if book==name:
                name=q
            else:
                pass 
    print('''
        What Do You want to Do?
        1- Sell a book
        2- Restock
        3-end
        ''')
    i=int(input('Enter any number: '))
    if i ==1:
        sell()
    elif i ==2:
        restock()
    elif i ==3:
        print('''
                Do you want to close the store?
                1- yes
                2-no
                ''')
        a = int(input('Enter the number: '))
        if a ==1:
            break
        else:
            pass