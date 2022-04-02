def circle():
    import math
    c = int(input('Enter the circumference of the circle: '))
    r= c/(2*math.pi)
    print('The radius of the circle is: ',r)
    print('The diameter of the circle is:',2*r)

circle()