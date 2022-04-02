def count():
    a= input('Enter a string: ')
    upper=0
    lower=0
    for l in a:
        if l.islower():
            lower += 1
        elif l.isupper():
            upper+=1
    print('The uppercase letters in the string are;',upper)
    print('The lowercase letters in the string are: ',lower)

count()