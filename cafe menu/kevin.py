# Arithmetic Operators(PEMDAS)
#Logical Operators(follows this order if there are multiple logical operators in a single statement NOT,AND,OR)
# gender = "Female"
# age = 12
# print(gender == "Male" or age == 12)#if one condition is true the output would be true(OR)
# print(gender == "Male" and age == 12)#both conditions must be true to get an output of true else false(AND)
# print(gender == "Female" and age == 12)
# print(gender == "Male" and age != 12)

#COnditional statements
#if condition :
#    statement     #indent 4times or use the tab key once

# age  = int(input())
# if age >= 18 and age <= 79:
#     print("You can drive")
# else:
#     print("You can't drive")



bill = 0
size_pizza = input("Enter L for large,M for medium and S for small: ")
add_pepperoni = input("Y for yes and N for no: ")
extra_chess = input("Y for yes and N for no: ")

# if size_pizza == "L" and add_pepperoni == "Y" and  extra_chess == "Y" :
#     print("Your bill is 135")
# elif size_pizza == "L" and add_pepperoni == "N" and  extra_chess == "Y" :
#     print("You bill is 125")
#     elif size_pizza == "L" and add_pepperoni == "N" and  extra_chess == "Y" :
#     print("You bill is 125")

if size_pizza == "L":   #nested ifs
    bill += 100
elif size_pizza == "M":
    bill += 85
else:
    bill += 50

if add_pepperoni == "Y":
        bill += 10

if extra_chess == "Y":
            bill += 5

print(f"Your total bill is {bill}")