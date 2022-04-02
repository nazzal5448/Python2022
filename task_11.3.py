import random
numbers=[]
for i in range(1,100):
    rnum=random.randint(1, 100)
    numbers.append(rnum)

for i in numbers:
    print('Frequency of',i,':',numbers.count(i),'\n')

