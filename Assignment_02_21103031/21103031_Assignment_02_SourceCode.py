# Question 01
# Program to utilize various built-in string functions or methods.

given_string = "Python is a case sensitive language"

print("\n", "The given string : ", given_string, "\n", sep='')

print("a. The length of the given string :", len(given_string))

print("b. The reverse of the given string :", given_string[::-1])

new_string = given_string[10:26]
print("c. The desired string after slicing the given string :", new_string)

replaced_string = given_string.replace("a case sensitive", "object oriented")
print("d. The desired replaced string :", replaced_string)

index_value = given_string.index("a")
print("e. The index of substring “a” in the given string :", index_value)

modified_string = given_string.replace(" ", "")
print("f. The string after removing white spaces from given string :", modified_string, "\n")

# Question 02
# Program to implement string formatting techniques in python.

student_name = "ANSH RAJ SHARMA"
student_ID = 21103031
department_name = 'Computer Science and Engineering'
student_CGPA = 9.5

formatted_string = "Hey, {} Here!\n" \
                   "My SID is {}\n" \
                   "I am from {} department and my CGPA is {}." \
                   .format(student_name, student_ID, department_name, student_CGPA)

print("\n", "The required formatted string is :\n", formatted_string, "\n", sep='')

# Question 03
# Program to make use of bitwise operators.

var_a = 56
var_b = 10

print("\n", "The given values are a = {} and b = {}.".format(var_a, var_b), "\n", sep='')

print("a. Bitwise AND (a,b) Output :", var_a & var_b)

print("b. Bitwise OR (a,b) Output :", var_a | var_b)

print("c. Bitwise XOR (a,b) Output :", var_a ^ var_b)

print("d. Bitwise Left shift")
print("   Left shift {} with 2 bits : {}".format(var_a, var_a << 2))
print("   Left shift {} with 2 bits : {}".format(var_b, var_b << 2))

print("e. Bitwise Right shift")
print("   Right shift {} with 2 bits : {}".format(var_a, var_a >> 2))
print("   Right shift {} with 4 bits : {}".format(var_b, var_b >> 4), "\n")

# Question 04
# Program to find the greatest of three numbers entered by the user.

num1 = int(input("\nEnter integer value 1 : "))
num2 = int(input("Enter integer value 2 : "))
num3 = int(input("Enter integer value 3 : "))

if (num1 >= num2) and (num1 >= num3):
    greatest_num = num1

elif (num2 >= num1) and (num2 >= num3):
    greatest_num = num2

else:
    greatest_num = num3

print("The greatest of the three integer numbers is :", greatest_num, "\n")

# Question 05
# Program to check if the word “name” is present in the string entered by the user.

input_string = input("\nEnter some text (string) : ")

if "name" in input_string:
    print("YES the \"name\" substring is there in the input text.", "\n")

else:
    print("NO \"name\" substring in the input text.", "\n")

# Question 06
# Program to check whether the given input lengths can form a triangle or not.

len1 = int(input("\nEnter the first side length of triangle (integer) : "))
len2 = int(input("Enter the second side length of triangle (integer) : "))
len3 = int(input("Enter the third side length of triangle (integer) : "))

if (len1 + len2 <= len3) or (len2 + len3 <= len1) or (len3 + len1 <= len2):
    print("\nNO Triangle can be formed with such side lengths.")

else:
    print("\nYES the triangle with such sides can be formed.")
