"""
def fibonaki():
    n = int(input("Enter Last Number : "))
    a = 0
    b = 1
    for n in range(2,n+1):
        f = a + b
        a=b
        b=f
        print(f)
fibonaki()

def factorial():

    n = int(input("Enter Last Number : "))
    if 0>n:
        print("Not Passibal")
    elif 0<n:
        x= 1
        for i in range(2,n+1):
            x=x*i
        print(x)
    else:
        print(1)
factorial()

for x in range(1,6):
    import random
    from random import randint
    Guest_Number = int(input("Enter Your Gest Number 1 To 9 : "))
    Random_Number =random.randint(1,9)
    if Guest_Number == Random_Number:
        print("You Are Win")
    else:
        print("You Are Loss")
        print("Random Number : ",Random_Number)

    x = int(input("Enter Any Number 1 To 9 : "))
    for x in range(1, x + 1):
        print(x * "*")

    Password = input("Enter Your Password: ")
    password = "siddik"
    if Password == password:
        print("Welcome")
    else:
        print("Again")

n=int(input( "the number of value a :"))
f0=0
f1=1
f2 = 1
print(f0)
print(f1)
sum=0
for i in range(1,n-1):
    fibo=f0+f1
    print(fibo)
    #sum = sum + fibo
    f0=f1
    f1=fibo

print("vai onik kosto kora fibonacci number ar summation paice :")



n = int(input())

if n % 2 != 0:
    if 1 <= n <= 99:
        print("Weird")

else:
    if n >= 2 and n <= 5:
        print("Not Weird")
    elif (n >= 6 and n <= 20):
        print("Weird")

    else:
        if n > 20:
            print("Not Weird")

a = int(input())
b = int(input())
print(a//b)
print(float(a/b))

year = int(input())
if year%4==0:
    print("True")
else:
    print("False")


n = int(input())
for i in range(1, n + 1):
    print(i, end="")

n = int(input())
j = ""
for i in range(1, n + 1):
    j = j + str(i)
print(j)


Year= int(input("Birthday Year : "))
Date = int(input("Birthday Date : "))
Mathe = int(input("Birthday Mathe : "))
Year1 = int(input("Enter Present Year : "))
Date1 = int(input("Enter Present Date : "))
Mathe1 = int(input("Enter Present Mathe : "))
x = Year1 - Year
y = Date1 - Date
z = Mathe1 - Mathe
print('your age is',x , " Year ",z, "Mathe" ,y, "Day")



Year= int(input("Birthday Year : "))
Date = int(input("Birthday Date : "))
Mathe = int(input("Birthday Mathe : "))
Year1 = int(input("Enter Present Year : "))
Date1 = int(input("Enter Present Date : "))
Mathe1 = int(input("Enter Present Mathe : "))
x = (Year1 - Year) - ((Mathe1 - Mathe) - (Date1 - Date))
y = Date1 - Date
z = (Mathe1 - Mathe)-(Date1 - Date)
print('your age is',x , " Year ",z, "Mathe" ,y, "Day")


sum=0
for i in range(1,(100+1)):
    sum= sum+i
print("Summation are=",sum)


x = frozenset({"a","b","c"})
print(x)

x = "sid \rdik"
print(x)

txt = "This will insert one \\ (backslash)."
print(txt)

txt = "This will insert one \ (backslash)."
print(txt)
txt = "Hello \f \f World!"
print(txt)

n = int(input("Enter Number :"))
x = 1

for i in range(1,n):
    x=(i+1)*x
    print(x)

x = "sid"
y= "s"
z = "d"
a = x + y + z
print(a)



i = int(input("Enter Any Number : "))
for i in range(2,i + 1):
    for j in range(2, i - 1 ):
        if i%j == 0:
            break
    else:
         print(i)
"""
sum=0
for i in range(1,100+1):
    if i%7 == 0:
        sum = sum + i
print(sum)
sum=0
i=[1,2,3,4]
print(type(i))
for x in i:
    sum = sum+x
print(sum)

a="siddik"
print(sorted(a,reverse=True))
a="siddik"
print(sorted(a))

My_list=[1,2,3,4]
My_list.sort(reverse=True)
print("sorted list in descending:-",My_list)

My_list="sid"
My_list.sort(reverse=True)
print("sorted list in descending:-",My_list)
print(a.__reversed__(a))