# print("hello world")

# name = input("what is your name :")
# print("hello,"+name)


# sum=10
# sum=100
# print(sum)


# name="john smith"
# age=20
# # new_old=True if name="johnsmith" else new_old=False
# is_new=True


# name=input("what is your name?")
# color=input("favourite color is ?")
# print("Hii"+name)
# print(name+" like "+color)


# type conversion
# Birth_year=input("birth_year:")
# age=2023-int(Birth_year)
# print(age)


# weight=input("enter your weight(pounds):")
# mass_kg=float(weight)*0.45
# print("weight in Kg "+ str(mass_kg)) 


# course='''
# Neel here
# UI/UX Designer
# Btech undergraudate
# DJSCE  '''
# print(course)


# course= "my sister name is priyal"
# print(course[0])

# course= "Python for beginner"
# print(course[0:4])

# course= "Python for beginner"
# print(course[0:-1])

# formatted string 
# name='Neel'
# last='gabani'
# msg=f'{name} <{last}> is a pro coder'
# print(msg)

#string methods 
# course= "Python for beginner"
# print(len(course))
# course.upper()
# print(course.upper())
# print(course.find('for'))
# print('for' in course)

# x=9.4
# print(round(x))
# y=-103.3
# print(abs(y))


# import math
# a=4.3
# print(math.ceil(a))

# is_hot=False
# is_cold=False

# if is_hot:
#     print("its hot day")
#     print("drink plenty of water")
# elif is_cold:
#     print("its cold day")
#     print("wear warm clothes")
# else:
#     print("its lovely day")
# print("enjoy your day")

# price=1000000
# has_good_credit=False

# if has_good_credit:
#     down_payment=0.1*price
# else:
#     down_payment=0.2*price
# print(f'down payment: ${down_payment}')


#comparsion operation
# name=input("enter your name:")
# print(len(name))

# if len(name) < 3:
#     print('name should be atleast of 3 letters')
# elif len(name) > 50:
#     print("name should be of max of 50 letters")
# else:
#     print('name looks good')


#weight calculator
# weight=int(input("enter your weight:"))
# unit=input("(L)bs or (K)g:")
# if unit.upper()=="L":
#     converted=weight*0.45
#     print(f'You are {converted} kilos')
# elif unit.upper()=="K":
#     converted=weight/0.45
#     print(f'You are {converted} pounds')


# while loop
# i=1
# while i<5:
#     print('*'*i)
#     i=i+1
# print('done!')

#for loop
# for item in 'python':
#     print(item)

# for item in ['neel','jigar','dhruvin','dhruv','krish']:
#     print(item)

# for item in range(10):
#     print(item)

# for item in range(2,50,3):
#     print(item)

#Nested loop
# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})')


# numbers =[5,2,5,2,2]
# for i in numbers:
#     print('x'*i)


# numbers =[2,2,2,2,5]
# for i in numbers:
#     output =""
#     for count in range(i):
#         output += 'x'
#     print(output)


# name =['bob','sarah','sachin','shubham','rohit','hardik']
# print(name[:4])

# to find max number
# no= [24,45,642,56,654,13,98,10]
# max=no[0]
# for i in no :
#     if i > max:
#         max= i
# print(max)

# 2D array
# matrix=[
#     [2,4,5],
#     [1,7,4],
#     [4,8,1]
# ]
# print(matrix)


#lists 

# number=[2,4,5,6,7,8,9]
# number.insert(0,1)
# number.append(20)
# print(number)

# wrong code (list without duplicate)
# number =[1,2,3,4,5,6,7,8,2]
# duplicate=2
# copy=number[0]
# for i in number:
#     copy += 1
#     if copy==duplicate:
#         number.remove(i)
#         print(number)


# numbers =[1,2,3,4,5,6,7,8,2]
# unique=[]

# for number in numbers:
#     if number not in unique:
#         unique.append(number)
# print(unique)


#### Tuples

# number=(1,3,4,5,6,5)
# print(number[4])


# unpacking 
# coordinates=[2,1,3,4,5]
# x,y,z,*rest= coordinates
# print(z)


#dictinaries 
# customer= {
#      "name": "neel",
#      "mail":"neelgabani@gmail.com",
#      "is_verfied": True
# }

# print(customer["name"])
# print(customer.get("birthdate",'1st jan'))


#exercise 
# phone = input("phone number:")
# digits_map= {
#     "1":"one",
#     "2":"two",
#     "3":"three",
#     "4":"four"
# }
# output=""
# for ch in phone:
#     output+= digits_map.get(ch,"!")+ ' '
# print(output)

#emoji converter 
# msg= input("> ")
# words=msg.split()
# emoji ={
#     ":)":"🙂",
#     ":(":"😟"
# }
# new_message=''
# for i in words:
#     new_message += emoji.get(i,i)+' '
# print(new_message)


#functions // parameters   ----> function should have return 
# to define the function as def name_function():

# def greeting(first_name):
#     print("good morning")
#     print(f'hii {first_name}')
#     print("welcome to the team")

# print("start")
# greeting('neel')
# print("finish")


# def square(number):
#     return number*number

# print(square(4))


# def emoji_converter(message):
#     words = message.split(" ")
#     emoji = {
#         ":)": "🙂",
#         ":(": "😟"
#     }
#     new_message = ''
#     for i in words:
#         new_message += emoji.get(i, i) + ' '
#     return new_message


# message= input("> ")
# print(emoji_converter(message))


# try and except
# try:
#     input=int(input('age: '))
#     print(input)
# except ValueError:
#     print('invalid input ')

## classes --> In classes while defining the class, The first letter is capitalised instead of using in the under scroll
# Unlike in naming of functions and variables, there we use under scroll
#An object is the instance of class
#Objects are actual instance of class based on blueprint
#Each object is a different instance of class

# class Point:
#     def __int__(self,x,y):   # to create new point object  # self--> point to current object
#         self.x=x
#         self.y=y

#     def move(self):
#         print('move')
#     def draw(self):
#         print("draw")


# point1=Point() # creating the object
# point1.x=10
# point1.y=20
# print(point1.x)
# point1.move()

# point=Point()
# point = Point(10,20) ---> error of argument in the point(10,20)
# point.x=12
# print(point.x)


# class Person:
#     def __init__(self,name):
#         self.name=name
#     def talk(self):
#         print(f'Hii, i am {self.name}')


# person_name= Person("neel gabani")  #---> person is not taking argument
# print(person_name.name)
# person_name.talk()

# person_name=Person("Neel gabani")
# person_name.talk()

# bob=Person("bob smith")
# bob.talk()


#Inheritance --> Technique to use the code again and again


# class Mammal:
#     def walk(self):
#         print("walk")
#
#
# class Dog(Mammal):
#     def balk(self):
#         print("balk")  # balk , walk ,talk, ---> are different methods
#
#
# class Cat(Mammal):
#     pass
#
#
# dog1=Dog()
# dog1.walk()


# modules

# import weight_cal

# from weight_cal import lbs_to_kgs
# print(lbs_to_kgs(25))


# print(weight_cal.lbs_to_kgs(40))


# random generating module 


# import random

# for i in range(3):
#     print(random.randint(10,100))
    
# print(random.random())


# import random
# class Dice:
#     def roll(self):
#         first=random.randint(1,6)
#         second = random.randint(1, 6)
#         return first,second
#
#
# dice= Dice()
# print(dice.roll())



# Absolute path
# c: \Program Files\Microsoft
# /usr/local/bin

# Relative Rath/ ---> Path starting from the current directory

from pathlib import Path
path = Path ()
for file in path.glob('*.py'): # glob to search file
    print(file)