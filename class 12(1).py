print('=================Task 1=================')
while True:
    print('Hey Sir! Welcome. It is an honour to serve you.')
    user=input('Do you want to shop or exit : \n')
    if user =='shop':
        pass
    elif user=='exit':
        break
    print ('What would you like to have?')
    choco =200
    ice = 200
    chips=200
    drinks= 200
    juices= 200
    customer=input('Chocolates, Juices, Ice cream, Chips ,Cold drink \n')
    if customer =='chocolate':
        print('Which one do you like?')
        flavour= input('dairy milk, perk, kitkat, twix, mars \n')
        choco-=1
        dairy_milk = 1
        perk= 40
        kitkat = 40
        twix =40
        mars= 40
        if flavour== 'dairy milk':
            dairy_milk-= 1
            print('Here is your dairy milk sir. Enjoy!')
        elif flavour =='perk':
            perk -= 1
            print('Here is your Perk sir. Enjoy!')
        elif flavour=='kitkat':
            kitkat-=1
            print('Here is your kitkat sir. Enjoy!')
        elif flavour=='twix':
            twix-=1
            print('Here is your twix sir. Enjoy!')
        elif flavour == 'mars':
            mars-=1
            print('Here is your mars sir. Enjoy!')
        else : 
            print ('Sorry sir! Try again.')
    elif customer == 'juice':
        print('Which one do you like?')
        apple=40
        slice = 40
        red_grapes = 40
        chounsa = 40
        orange =40
        flavour= input('Slice, Apple, Red grapes, Chounsa, Orange \n')
        if flavour =='slice':
            slice-= 1
            print('Here is your slice sir. Enjoy!')
        elif flavour=='apple':
            apple-=1
            print ('Here is your Apple juice sir. Enjoy!')
        elif flavour== 'orange':
            orange-= 1
            print('Here is your orange juice sir. Enjoy!')
        elif flavour =='red grapes':
            red_grapes -= 1
            print('Here is your red grapes juice sir. Enjoy!')
        elif flavour=='chounsa':
            chounsa-=1
            print('Here is your chounsa juice sir. Enjoy!')
        else : 
            print ('Sorry sir! Try again.')
    elif customer=='ice cream':
        print('Which one do you like?')
        flavour=input('mango, pista, orange,vanilla,rainbow \n')
        mango=40
        pista=40
        rainbow=40
        orange=40
        vanilla=40
        if flavour== 'pista':
            pista-= 1
            print('Here is your pista ice cream sir. Enjoy!')
        elif flavour =='mango':
            mango -= 1
            print('Here is your mango ice cream sir. Enjoy!')
        elif flavour=='rainbow':
            rainbow-=1
            print('Here is your rainbow ice cream sir. Enjoy!')
        elif flavour=='orange':
            orange-=1
            print('Here is your orange ice cream sir. Enjoy!')
        elif flavour == 'vanilla':
            vanilla-=1
            print('Here is your vanilla ice cream sir. Enjoy!')
        else : 
            print ('Sorry sir! Try again.')
    elif customer=='chips':
        print('which one do you like?')
        flavour=input('lays, kurkure, asli baba , kurleez, wavy \n')
        lays=40
        kurkure=40
        wavy=40
        kurleez=40
        asli=40
        if flavour== 'lays':
            lays-= 1
            print('Here is your lays sir. Enjoy!')
        elif flavour =='asli baba':
            asli -= 1
            print('Here is your asli baba sir. Enjoy!')
        elif flavour=='kurkure':
            kurkure-=1
            print('Here is your kurkure sir. Enjoy!')
        elif flavour=='kurleez':
            kurleez-=1
            print('Here is your kurleez sir. Enjoy!')
        elif flavour == 'wavy':
            wavy-=1
            print('Here is your wavy sir. Enjoy!')
        else : 
            print ('Sorry sir! Try again.')
    elif customer=='cold drink':
        print('Which one do you like?')
        flavour=input('pepsi, marinda, 7up, sprite, deo \n')
        deo=40
        sprite=40
        pepsi=40
        up=40
        marinda=40
        if flavour== 'pepsi':
            pepsi-= 1
            print('Here is your pepsi sir. Enjoy!')
        elif flavour =='marinda':
            marinda-= 1
            print('Here is your marinda sir. Enjoy!')
        elif flavour=='sprite':
            sprite-=1
            print('Here is your sprite sir. Enjoy!')
        elif flavour=='7up':
            up-=1
            print('Here is your 7up sir. Enjoy!')
        elif flavour == 'deo':
            deo-=1
            print('Here is your deo sir. Enjoy!')
        else : 
            print ('Sorry sir! Try again.')
print('Thank you! Have a nice day.')        
        