class Computation:
    import math
    def __init__(self):
        pass

    def Factorial(self, number):
        print(self.math.factorial(number))

    def sum(self,num):
        n=[]
        for i in range (1,num):
            n.append(i)
        print(self.math.fsum(n))

    def testPrime(self,a):
        if a>1:
            for i in range(2,a):
                if (a%i==0):
                    print(a,'is not prime')
                    break
                else:
                    print(a,'is prime.')
                    break
    
    def testPrimes(self, num1, num2):
        l=[]
        for i in range(num1,num2):
            l.append(i)
        for n in l:
            for i in range (2,n):
                if (n%i==0):
                    print(n,'is not prime')
                    break
                else:
                    print(n,'is prime.')
                    break

    def tableMult(self,num):
        for i in range(1,16):
            print(i*num,'/n')

    def allTablesMult(self):
        for i in range(1,9):
            for x in range (1,16):
                print(i*x, '/n')
    
    def listDiv(self,num):
        ldiv=[]
        for i in range(1,num):
            if num%i==0:
                ldiv.append(i)
        print (ldiv)

    def listDivPrime(self,num):
        ldiv=[]
        for i in range(1,num):
            if num%i==0:
                for x in range(2,i):
                    if i%x==0:
                        break
                    else:
                        ldiv.append(i)
                        break
            else:
                pass
        
        print (ldiv)
math= Computation()
# math.sum(90)
# math.testPrime(70)
# math.testPrimes(20, 80)
math.listDiv(90)
math.listDivPrime(90)

