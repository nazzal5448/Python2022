print('==============Task 1==============')
import statistics
def mean(*a):
    a1= len(a)
    b= sum(a)
    print(b/len(a))
    
mean(9,8,7,6,5,4)

def median(*a):
    l=[]
    for a1 in a:
        l.append(a1)
    m=statistics.median(l)
    print(m)
    
def mode(*a):
    b=[]
    for a1 in a:
        b.append(a1)
    m= statistics.mode(b)
    print(m)
    
mode(9,7,6,5,7,7,8,0)
median(9,8,7,6,5,4,3,2)