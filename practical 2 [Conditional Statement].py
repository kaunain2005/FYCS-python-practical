#Question 1. write a program to calculate perimeter and area of square and rectangle.
length=int(input("Enter a length of rectangle :"))
breadth=int(input("Enter a breadth of rectangle :"))
sides_length=int(input("Enter a length of sides of square :"))
area_recangle = breadth*length
perimeter_rectangle = 2*(length+breadth)
area_square = sides_length*sides_length
perimeter_sqauare = 4*sides_length
print('Area of rectangle is :',area_recangle)
print('Perimeter of rectangle is :',area_recangle)
print('Perimeter of square is :',perimeter_sqauare)
print('Area of square is :',area_square)

#Question 2. write a program to accept two numbers and find the greatest number among two numbers.
a=int(input('Enter a first number :'))
b=int(input('Enter a second number :'))
if a!=b:
    if a>b:
        print(a,'is greater number')
    else:
        print(b,'is greater number')
else:
    print("Both are equal")

#Question 3. write a program to accept three numbers and print the smallest number among the three numbers.
n1=int(input('Enter a first number :'))
n2=int(input('Enter a second number :'))
n3=int(input('Enter third number :'))
if n1<n2:
    if n1<n2:
        print(n1,"is smallest")
    else:
        print(n3,"is smallest")
else:
    if n2<n3:
        print(n2,"is smallest")
    else:
        print(n3,"is smallest")

#Question 4. write a program to accept a year from user and check whether the given year is leap year or not.
year=int(input("Enter a year :"))
if year%4==0:
    print("It is leap year.")
else:
    print("It is not a leap year.")

#Question 5. write a program to check whether the enter number is positive or negative.
num=int(input("Enter a number :"))
if num>=0:
    print("Number is positive.")
else:
    print("Number is negative.")

#Question 6. write a program to check whether the entered number is odd or even.
num=int(input("ENter a number :"))
if num%2==0:
    print("It is an even number.")
else:
    print("It is odd number.")

#Question 7. write a program to calculate area of circle by accepting radius from user and calculate the area when the radius is positive as show invalid.
radius=int(input("Enter a radius :"))
if radius>0:
    area=3.14*radius*radius
    print("Area of circle is :",area)
else:
    print("Invalid radius!")
