#Question 1.Write a program to display different data types in Python.
a=90
print(a)
b=5.5
print(b)
c="Hello"
print(c)

#Question 2. Write a program to accept two numbers and perform basic arithmetic operations on that numbers.
a=int(input("Enter a First Number : "))
b=int(input("Enter a Second Number: "))
print('Sum of numbers :',a+b)
print('Difference of numbers :',a-b)
print('Product of numbers :',a*b)
print('Division of numbers :',a/b)
print('Mod of numbers :',a%b)

#Question 3. write a program to calculate volume of square.
r=int(input("Enter a radius :"))
v=3.14*(4/3)*r**3
print("Volume of Sphere is :",format(v,"0.2f"))

#Question 4. write a program to calculate simple interest.
p=int(input("Enter a Principal value :"))
n=float(input("Enter a Period of investment :"))
r=float(input("Enter a rate of interest :"))
simple_interest=(p*r*n)/100
print("Simple interest is :",simple_interest)

#Question 5. write a program to accept time in minutes and convert it into hours and minutes.
m=int(input('Enter a time in minutes :'))
t=m//60
m=m%60
print('Time in hours and minutes is :',t,":",m)

#Question 6. write a program to convert temperature in degree to fahrenheit and fahrenheit to degree.
celcius=float(input("Enter a temperature in celcius :"))
f=(celcius*9/5)+32
print("Temperature in Fahrenheit is :",f)
fahrenheit=float(input("Enter a temperature in fahrenheit :"))
c=(fahrenheit-32)*5/9
print("Temperature in Celcius is :",c)

#Question 7. write a program to calculate speed of car by accepting distance  covered by the car and time required for journey.
distance=int(input("Enter a distance in km :"))
time=int(input("Enter a time in hours :"))
speed=distance/time
print('Speed of the car is :',speed)
