# Question 01
# A Recursive Python function to solve the problem of tower of Hanoi.

def tower_of_hanoi(disks, source, auxiliary, destination):
    if disks == 1:
        print(f"Move disk 1 from {source} to {destination}.")
        return

    tower_of_hanoi(disks-1, source, destination, auxiliary)
    print(f"Move disk {disks} from {source} to {destination}")
    tower_of_hanoi(disks-1, auxiliary, source, destination)


# Here n represents the number of disks entered by the user.

n = int(input("Enter the number of disks: "))

while n <= 0:
    print("\nERROR!! The number of disks cannot be negative or Zero.")
    print("Enter a valid number!!\n")
    n = int(input("Enter the number of disks: "))

# Here letter represents:
#   'A' = Source Rod
#   'B' = Auxiliary Rod
#   'C' = Destination Rod

tower_of_hanoi(n, 'A', 'B', 'C')

# Question 02
# A Python program to print the Pascal’s triangle for n number of
# rows given by the user using both recursive and iterative procedures.

# METHOD 01 | USING RECURSIVE PROCEDURES
print("USING RECURSIVE PROCEDURES")
rows = int(input("Enter the number of rows (Positive Integer) : "))

# 'n' parameter collects rows entered by the user.


def pascal_triangle(n):

    if n == 0:
        print("Enter a positive integer value")
        return []
    elif n == 1:
        return [[1]]
    else:
        next_row = [1]
        result = pascal_triangle(n-1)
        previous_row = result[-1]

        for loop in range(len(previous_row) - 1):
            next_row.append(previous_row[loop] + previous_row[loop+1])

        next_row += [1]
        result.append(next_row)

        return result


print("The Pascal Triangle of %d rows is :" % rows)
output = pascal_triangle(rows)

# Here again i and j are looping variable.
# to display the output in the given pattern.

for i in range(rows):

    # j iterated for columns to specify spaces.
    for j in range(rows-i-1):
        print(format(" ", "<2"), end="")

    # j iterated for columns to specify numbers of Pascal Triangle.
    for j in range(i+1):
        print(format(output[i][j], "<3"), end=" ")

    print()

# METHOD 02 | USING ITERATIVE APPROACH 'for' LOOP
print("\nUSING ITERATIVE APPROACH 'for' LOOP")
rows = int(input("Enter the number of rows (Positive integer) : "))

list_1 = []

# Here i and j are looping variables.
# i correspond to row and j to columns.

for i in range(rows):
    list_2 = []
    for j in range(i + 1):
        if j == 0 or j == i:
            list_2.append(1)
        else:
            list_2.append(list_1[i-1][j-1] + list_1[i-1][j])
    list_1.append(list_2)

print("The Pascal Triangle of %d rows is :" % rows)

# Here again i and j are looping variable.
# to display the output in the given pattern.

for i in range(rows):

    # j iterated for columns to specify spaces.
    for j in range(rows-i-1):
        print(format(" ", "<2"), end="")

    # j iterated for columns to specify numbers of Pascal Triangle.
    for j in range(i+1):
        print(format(list_1[i][j], "<3"), end=" ")

    print()

# Question 03
# Input two integer values from user, calculate and print the quotient
# and reminder obtained from the two values, and perform following operations.
# Use built-in functions only


def display(q, r):
    # Here q = quotient, r = remainder
    print("The quotient is :", q)
    print("The remainder is :", r)


dividend = int(input("Enter dividend (positive integer) : "))
divisor = int(input("Enter divisor (positive integer) : "))

quotient, remainder = divmod(dividend, divisor)
display(quotient, remainder)
func = display

print("\na. Checking whether function/values is callable or not.")
print("Check the source code to see which value and function is used in callable method.")
print(callable(dividend))
print(callable(func))

print("\nb. Checking whether all the values are non zeros or not")
# all() returns:
# 1) True : if all elements in iterable are true.
# 2) False : if any element in iterable is false.

output_dict = {quotient: "Quotient", remainder: "Remainder"}
check = all(output_dict)
print("The previous output is :", output_dict)
print("The output is :", check)

if check:
    print("The quotient and remainder are non zero values.")
else:
    print("The quotient or remainder or both are zero.")

print("\nc. Adding values (4, 5, 6) to the result and filtering out the values which "
      "are greater than 4.")

# list_1 contains values after adding quotient and given tuple elements.
list_1 = []

# list_2 contains values after adding remainder and given tuple elements.
list_2 = []

for loop in (4, 5, 6):
    list_1.append(quotient + loop)
    list_2.append(remainder + loop)

list_3 = list_1 + list_2

filtered_list = list(filter(lambda x: (x > 4), list_3))

print("The required filtered values in list form is :", filtered_list)

print("\nd. Converting the above list into set datatype.")
filtered_set = set(filtered_list)
print("The required output is :", filtered_set)

print("\ne. Making above set immutable.")
immutable_set = frozenset(filtered_set)
print("The immutable set is :", immutable_set)

print("\nf. Finding maximum value from set and its hash value.")
max_value = max(immutable_set)

print("(1) The maximum value from the set is :", max_value)
hash_value_1 = hash(max_value)
hash_value_2 = hash(immutable_set)

print("(2.a) The hash value of {} is: {}".format(max_value, hash_value_1))
print("(2.b) The hash value of {} is: {}".format(immutable_set, hash_value_2))

# Question 04
# Python Program to create a class named Student, use the_init_() function to assign
# values for name and roll number. And also call _del_() function to
# destroy object that is created.


class Student:
    def __init__(self, name, roll_num):
        self.student_name = name
        self.student_roll_num = roll_num


# Here two Student objects are created.

student_1 = Student('ABC', 1001)
student_2 = Student('DEF', 1002)

# Displaying student details.
print("Student_1 details are as follow: ")
print("Name :", student_1.student_name, "\t", "Roll Number :", student_1.student_roll_num)

print("\nStudent_2 details are as follow: ")
print("Name :", student_2.student_name, "\t", "Roll Number :", student_2.student_roll_num)

# Deleting student_1 object using del statement.
del student_1

# Try to run below code. You will get NameError.
# print(student_1)

# Question 05
# A Python program to store details of three employees: name and salary
# using class and making required modifications.


class Employee:

    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def employee_details(self):
        print("Name :", self.name, ", Salary :", self.salary)


# Creating instances of class Employee.
# Here letter 'e' is used as a variable name for employee.

e1 = Employee("Mehak", 40000)
e2 = Employee("Ashok", 50000)
e3 = Employee("Viren", 60000)

print("The total employee are :", Employee.count)
print("The employee details are :")

e1.employee_details()
e2.employee_details()
e3.employee_details()

# (a) Updating the salary of Mehak to 70000.
e1.salary = 70000

print("\n(a) The updated details are:")

e1.employee_details()
e2.employee_details()
e3.employee_details()

# (b) Deleting the record of employee Viren.
del e3

print("\n(b) The modified records are:")
e1.employee_details()
e2.employee_details()

# Employee 3 has been deleted hence the below code will generate NameError.
# e3.employee_details()

# Question 06
# A Python program that depicts a situation. Writing a piece of code for shopkeeper
# to use so that the test runs smoothly.

flag = 'Y'
while flag == 'Y':

    def output_string(input_list):
        return ''.join(input_list)


    def permutation(lst, start, end):
        if start == end:
            main_list.append(output_string(lst))
        else:
            for loop in range(start, end + 1):
                lst[start], lst[loop] = lst[loop], lst[start]
                permutation(lst, start + 1, end)
                lst[start], lst[loop] = lst[loop], lst[start]


    print("Welcome to the game of 'TEST THE FRIENDSHIP'.")
    print("Let's begin...")
    print("It's a two player game.")

    print("Select your player one will be 'George' and other will be 'Barbie'.")

    print("\nGeorge, it's Your Turn.")

    main_list = []
    main_string = input("Enter a word George (lowercase) : ")

    n = len(main_string)
    char_of_string = list(main_string)
    permutation(char_of_string, 0, n - 1)

    print("\nBarbie, Your Turn...")
    print("Barbie you need to create a new word using the exact same letters as George.")
    test_string = input("Enter a word Barbie (lowercase) : ")

    if test_string in main_list:
        print("\nYou are True Friends.")
        print("As you entered word that matches one of the combinations given here:")
        print(main_list)
        print()
    else:
        print("\nYour friendship is a fake.")
        print("Barbie, your word didn't match any combination from the list given here:")
        print(main_list)
        print()

    print("Do you want to play again? (Y/N) : ", end="")
    flag = input()
