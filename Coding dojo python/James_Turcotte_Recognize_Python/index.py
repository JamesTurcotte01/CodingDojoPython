num1 = 42  #variable declaration
num2 = 2.3 #variable declaration
boolean = True  #data Type, primitive, boolean
string = 'Hello World'  #primitive, data type
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #composite list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration/ composite tuples 
fruit = ('blueberry', 'strawberry', 'banana') #composite dictionary
print(type(fruit)) #calling the function to print var(fruit)
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') #add value "mushrooms" to pizza_toppings
print(person['name']) #print persons name from object person. "john"
person['name'] = 'George' #tuples change name in person object to "george"
person['eye_color'] = 'blue' #add to variable
print(fruit[2]) #log statemnt



if num1 > 45: #if statement/ conditional
    print("It's greater") #log statement
else: #else statement/ conditional
    print("It's lower") #log statement

if len(string) < 5: #if statement/ conditional
    print("It's a short word!") #log statement
else if(string) > 15: #else if/ conditional
    print("It's a long word!")  #log statement
else:   #else statement/ conditional
    print("Just right!") #log statement

for x in range(5): #for loop start
    print(x) #log statement
for x in range(2,5): #for loop start
    print(x) #log statement
for x in range(2,10,3): #for loops start
    print(x) #log statement
x = 0 #variable declaration of data type number
while(x < 5): #while loop start
    print(x) #log statement
    x += 1 #variable declration

pizza_toppings.pop() #tuple delete all values
pizza_toppings.pop(1) #tuple delete value

print(person) #log statement
person.pop('eye_color') #delete eye_color from person
print(person) #log statement

for topping in pizza_toppings: #for loop in composite list
    if topping == 'Pepperoni': #if statement
        continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #if statement

        break #for loop break

def print_hello_ten_times(): #function 
    for num in range(10): #for loop
        print('Hello') #log statement

print_hello_ten_times() #log statement

def print_hello_x_times(x): #function 
    for num in range(x): #for loop
        print('Hello') #log statement

print_hello_x_times(4) #call function

def print_hello_x_or_ten_times(x = 10): #function
    for num in range(x): #for loop
        print('Hello') #log statement
print_hello_x_or_ten_times() #log statement
print_hello_x_or_ten_times(4) #log statement


"""
Bonus section #multiline comment
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)