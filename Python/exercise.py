
#Exercise 1
full_name = 'John Smith'
age = 20
is_new = True

#Exercise 2
name = input('Enter your name ')
color = input('What is your favourite color? ')
print(name+" likes "+color)

#Exercise 3
weight = int(input('Enter weight in pounds '))
kg = weight * 0.45359237;
print(kg)

#Exercise 4
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payemnt = 0.1 * price
else:
    down_payemnt = 0.2 * price
print(f"Down payment: ${down_payemnt}")

#Exercise 5
weight = int(input('Enter weight'))
unit = input('Select "L" for pounds or "K" for kg')
if unit.upper()=='L':
    value = weight * 0.45
    print(f"Kilos: {value}")
elif unit.upper()=='K':
    value = weight / 0.45
    print(f"Pounds: {value}")
else:
    print("Invalid choice")

#Exercise 6
prices = [10,40,70]
total_cost=0
for price in prices:
    total_cost+=price
print(f"Total cost of items: ${total_cost}")

#Exercise 7
numbers = [5,2,5,2,2]
for i in numbers:
    print("x"*i)

#Exercise 8
numbers =[3,7,9,2]
max = numbers[0]
for number in numbers[1:]:
    if number>max:
        max=number
print(max)

#Exercise 9
list = [2,3,6,2,3,5,9]
uniques=[]
for num in list:
    if num not in uniques:
        uniques.append(num)
print(uniques)

#Exercise 10
num ={"1":"one","2":"two","3":"three"}
output=""
phone = (input("Phone: "))
for ch in phone:
    output+=num.get(ch,"!")+" "
print(output)

#Exercise 11
message = input(">")
emojis={":)":"😊",
        ":(":"😕"
}
words = message.split(" ")
output=""
for word in words:
    output+=emojis.get(word,word)+" "
print(output)

#Exercise 12
class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f"{self.name} is talking..")

person = Person("XYZ")
person.talk()

#Exercise 13
import random


class Dice:
    def roll(self): 
        first = random.randomInt(1,6)
        second=random.randomInt(1,6)
        return first, second
    
        
dice = Dice()
print(dice.roll())





