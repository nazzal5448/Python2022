import random
def who():
    assumptions=['You are very kind and generous.',
                'You love the people around you',
                'You are not selfish and always love mankind.',
                'You never leave those who need you.',
                'You are a hardworking and ambitious person.']
    user=random.choice(assumptions)
    print(user)

def colour():
    assumptions=['Yellow, which means you are smart, creative and good in communication',
                 'pink, which means you are romantic, kind and optimistic.',
                 'red,which means you are energatic,courageous and extrovert.',
                 'blue,which means you are enthusiastic, sympathetic and idealistic.']
    user=random.choice(assumptions)
    print('The colour of your personality is',user)

def meaning():
    assumptions=['Your name means a ruler who rules over the hearts.',
                 'Your name refers to a king who was known for his bravery.',
                 'your name means a person with extra beauty and shine.',
                 'Your name refers to lion.',
                 'Your name means generous and always down for love.']
    user=random.choice(assumptions)
    print(user)

while True:
    a=input('''
          Which game do you want to play?
          1. Who are you?
          2.Colour of your personality
          3.Meaning behind your name
          ''')

    if int(a)==1:
        who()
    elif int(a)==2:
        colour()
    elif int(a)==3:
        meaning()
    else:
        print('Invalid Input!')

    ex=input('''
             Do you Want to exit?
             1.Yes
             2.NO
             ''')
    if int(ex)==1:
        print('Game exited successfully!')
        break
    elif int(ex)==2:
        pass
    else:
        print('Invalid Input!')