a= [['happy','BirtHday','to','yoU'],['this','Is','MY','BdaY','Month'],['wish','me','HappY','BirtHday']]

def upper(a):
    b=[]
    c=[]
    d=[]
    e=[]
    for l in a:
        if l==a[0]:
            for l1 in l:
                b.append(l1.upper())
            e.append(b)
        elif l==a[1]:
            for l1 in l:
                c.append(l1.upper())
            e.append(c)
        elif l==a[2]:
            for l1 in l:
                d.append(l1.upper())
            e.append(d)
        else:
            pass
    print(e)
     

upper(a)
