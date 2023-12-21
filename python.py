#! /usr/bin/python

import requests

print("Content-type: text/html")
print("")

print("<h1>Hello World!</h1>")

age = 22
print(age)

name = "Hazel"
print(name)

print(age + 5)

number = "5"
pi = 3.1415
print(int(number) * pi) #casting

string = "My name is"
print(string[1:5])

myList = ["Mel", "Juru", "Gretch", "Jess"]
print(myList)
print(myList[2])
print(myList[0:2])
myList.append("Maya")
print(myList)

myTuple = ("Gina", "Tina", "Luna")
# myTuple.append("Catarina")

ssns = {}
ssns["102-03"] = "Gina"
ssns["199-99"] = "Tina"
ssns["999-00"] = "Luna"
print(ssns)
print(ssns["999-00"])

print("Repetition")

x = 0
while x<=10:
    print(x)
    x = x + 1
print("Done")

for i in range(10):
    print(i)

for ssn in ssns:
    print(ssn + " belongs to " + ssns[ssn])

for ssn, name in ssns.items():
    print(ssn + " belongs to " + name)

print("Making decisions")

num = 1
if num == 0 or num == 1:
    print("Number is indeed 0 or 1")
else:
    print("Number is not 0 or 1")

if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

for num in range(2, 10):
    isPrime = True
    for divisor in range(2, num):
        if num % divisor == 0:
            isPrime = False
    if isPrime: #== True:
        print(num)

print("Managing Code - functions")

def log(msg):
    msg = str(msg)
    msg = msg + "<br />"
    print(msg)

age = 22
name = "Hazel"
ssn = "102-03"

log(age)
log(name)
log(ssn)

print("Managing Code - objects")

class Game:
    def __init__(self): #constructor
        self.nums = []
    def startGame(self):
        print("We are starting now... <br />")
    def addNum(self, num):
        self.nums.append(num)
    def printNums(self):
        print("List of numbers: ", self.nums)
g = Game()
g.startGame()
g.addNum(54)
g.printNums()

print("Getting data from web")

response = requests.get('https://catfact.ninja/fact')
#print(response.text)

response = response.json()
print(response['fact'])