#print the number is positive or negative#
'''
n=int(input("enter the number:"))
if (n>0):
    print("the given no is positive:",n)
else:
    print("The given no is negative:",n)
'''
#print the given no is odd or even#
'''
n=int(input("enter the number:"))
if (n%2 ==0):
    print("the given no is even:",n)
else:
    print("The given no is odd:",n)
'''

'''
n=int(input("enter the number:"))
if (n >10):
    print("The given no is greater then 10:",n)
elif(n<10):
    print("The given no is lesser then 10:",n)
else:
    print("entered number is equal to 10:",n)
'''
#divisible by 5#
'''
n=int(input("enter the number:"))
if (n%5 ==0):
    print("The given no is divisible by 5:",n)
else:
    print("The given no is not divisible by 5:",n)
'''
#print if it is multiple of 7
'''
n=int(input("enter the number:"))
if (n%7 ==0):
    print("The given no is multiple of 7:",n)
else:
    print("The given no is not multiple of 7:",n)
'''
#find the number is greater then or lesser then
'''
a=int(input("Enter the number a:"))
b=int(input("Enter the number b:"))
if (a>b):
    print("a is greater then b:",a)
elif (b>a):
    print("b is greater then a:",b)
else:
    print("both are equal:")
'''
'''
a=int(input("Enter the number a:"))
b=int(input("Enter the number b:"))
c=int(input("Enter the number c:"))
if((a>=b) and (a>=c)):
    if(b>=c):
        print("\n decending order:"a,b,c)
        print("\n ascending order:"c,b,a)
    else:
        print("\n decending order:"a,c,b)
        print("\n ascending order:"b,c,a)
elif ((b>=a) and (b>=c)):
    if (a >= c):
        print("\n decending order:"b,a,c)
        print("\n ascending order:"c,a,b)
    else:
        print("\n decending order:"b,c,a)
        print("\n ascending order:"a,c,b)
elif((c>=a) and (c>=b)):
    if(a>=b):
        print("\n decending order:"c,a,b)
        print("\n ascending order:"b,a,c)
    else:
        print("\n decending order:"c,b,a)
        print("\n ascending order:"a,b,c)
'''
'''
a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant: "))
x= b*b-4*a*c
r1=(-b+x)/2*a
r2=(-b-x)/2*a
'''
n=int(input("enter the no:"))
i=1
while (i<n):
    i+=1
    print(i)