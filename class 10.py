medical=['bio', 'humanity', 'discipline', 'helping people']
engineering=['maths', 'problem solving', 'logical', 'statistics', 'accounting','technology', 'computer']
arts=['management', 'writing','creative','linguistics','literature','drawing','painting','acting']
interests=input('Tell me about your interests: \n')

if interests in medical:
    print('You Will do better in medical fields.')
    
elif interests in engineering:
    print('You better persue your studies in engineering.')
    
elif interests in arts:
    print ('You should study arts. It matches your interests.')
    
else:
    print('I need to know more.')
    