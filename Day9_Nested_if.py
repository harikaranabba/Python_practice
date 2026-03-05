#nested if

age=21
eat_pizza= True
workout= False
if(age<30):
    if eat_pizza:
        print("Unfit")
    else:
        print("Fit")
else:
    if workout:
        print("Fit")
    else:
        print("Unfit")

#Ternary operator
print("child") if (age<21) else("adult")
print("unfit" if(eat_pizza) else "fit") if (age>30) else("fit" if(workout) else "unfit")

#quizz
age=24
income=50000
if age < 18:
    message="you are too young to work"
elif age >= 18 and age <=25:
    if income <30000:
        message="you are eligible for a student discount"
    else:
        message="you are eligible for a regular discount"
else:
    message="you are eligible for a regular discount"
print(message)


#Odd or Even

num = int (input("enter the num:"))
if(num % 2==0):
        print (num,"is an even number")

else:
    print(num,"is an odd number")



#using_ternary_operator
"""
num=int(input("enter the number:"))
print("even" if(num%2==0) else("Odd"))
"""
    



    

