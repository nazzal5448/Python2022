import random
print('===============Random Colour Hex Generator=============')
colour= ['red','yellow','green','blue','pink','black','white','purple','brown']
print(random.choices(colour,k=3))

print('===============Random multiple of 7================')
integer= random.randrange(0, 70,7)
if (integer>0):
    print(integer)
else:
    print('0 is not a multiple of 7.')

print('================Random Alphabetic String=============')
alps=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
string= random.choices(alps,k=5)
print(string)

print('==============Random Integer Generator==============')
integer=random.randint(10, 100)
print(integer)
