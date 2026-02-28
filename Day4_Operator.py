#Arithmstic Operator
print(10+5*3)
print(20-10/5*2)
print(20-2.0*2)

a = 75
b = 14
print(a/b)
print(a//b)
print(a%b)

#to find a to the power b
a = 25
b = 6
c = a**b
print(type(c),c)

print(2*3*(2%10))
#the above calculation is done as following
print(2%10)    #2
print(3**2)    #9
print(2**9)    #512

#relational Operator

a = 25
b = 12
print(a<b)
print(a>b)
print(a>=b)
print(a==b)
print(a!=b)
a = b
print(a==b)

#quiz
a = "Hari"
b = "hari"
print(a==b)
print(a<b)

#ASCII value
print("H:",ord('H'))
print("h:",ord('h'))
print(a<b)

a = "Nishu"
b = "Nisha"
print(a==b)
print(a<b)
print("u:",ord('u'))
print("a:",ord('a'))
print(a>b)

#AUGMEMNTED OPERATORS
a = 15
b = 25
a = a+2
print(a)
a = a+b
print(a)
a += 2
b *= 3
print("a =",a,"b =",b)
b /= 5
print(b)
b %= 4
print(b)

#Quiz(Augmented Operators)-Bank Acc
name, balance = "Hari",500.0
print("Before Intrest:",balance)
#Update the balance with 7% interest
balance += (7/100 * balance)
print("After Intrest:",balance)

#MEMBERSHIP OPERATOR
list = [1,2,3,4,'5',6]
print(2 in list)
print(9 in list)
print(9 not in list)
print(5 in list)
print('5' in list)
name = 'HariKaran'
print('H' in name)
print('K' in name)


