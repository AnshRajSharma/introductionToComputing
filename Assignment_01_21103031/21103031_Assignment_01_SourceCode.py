# Question 01
# Program to find average of three numbers entered by user.

num1 = int(input("Enter Number 1 (integer) : "))
num2 = int(input("Enter Number 2 (integer) : "))
num3 = int(input("Enter Number 3 (integer) : "))

average = (num1 + num2 + num3)/3

print("The average of three numbers above is : ", "{:.2f}".format(average), "\n")

# Question 2
# Program to compute a person's income tax.

tax_Rate = 0.2
standard_Deduction = 10000
dependent_Deduction = 3000

gross_Income = int(input("Enter your Gross Income (Integer) (Rs.) : "))
dependents = int(input("Enter the number of dependents : "))

taxable_Income = gross_Income - standard_Deduction - (dependent_Deduction * dependents)
tax = taxable_Income * tax_Rate

print("Your income tax is (Rs.) :", "{:.2f}".format(tax), "\n")


# Question 3
# Program to store different data type values into a list.

Student = ['SID', 'Name', 'Gender', 'Department', 'CGPA']

print("The Student List Format :", Student)

Student[0] = 21103031
Student[1] = 'ANSH RAJ SHARMA'
Student[2] = 'M'
Student[3] = 'Computer Science and Engineering'
Student[4] = 9.2

print("The required Student list is :", Student, "\n")

# Question 4
# Program to enter marks of 5 students into a list and display them in sorted manner.

Marks = [70, 60, 90, 80, 100]

print("The Marks list of 5 students is :", Marks)
print("The Marks list is sorted in ascending order as :", sorted(Marks))
print("The Marks list is sorted in descending order as :", sorted(Marks, reverse=True), "\n")

# Question 5
# Program to print a specified list after removing 4th element.

Color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("The Color List :", Color)
removed_Element = Color.pop(3)
print("The removed element from the Color List :", removed_Element)
print("The Modified List :", Color, "\n")

# Removed ‘Black’ and ‘Pink’ from the list and replaced them with ‘Purple’.

Color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("The Original Color List :", Color)
Color[3:5] = ['Purple']
print("The Modified List :", Color)
