#swapping
a=10
b=20
print(a,b)

#code
temp=a
a=b
b=temp
print(a,b)

#using in multiple assing
a=10
b=20
a,b=b,a
print(a,b)

#Augmented operator
a=5
b=7
print(a,b)
#after
a+=2
b-=2
print(a,b)

name,balance="Hari",1000
print("befor intrest:",balance)

#update balance with 9% intrest

balance +=(9/100*1000)
print("after intre:",balance)




