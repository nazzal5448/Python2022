print('=============Rolling Dice Game============')
import random
attempt=1
while attempt<=3:
    characters=[1,2,3,4,5,6]
    user=random.choices(characters,k=2)
    print(user)
    if user[0]==user[1]:
        print('You Won!')
        break


    elif attempt==3:
        print('You Failed!')
        break
    else:
        attempt+=1