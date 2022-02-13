# Question 01
# Python program to count the number of occurrences of each word or
# character in the string entered by the user. (Count the Number of Occurrences
# of each character only if the single word is entered by the user).

flag = 'Y'
while flag == 'Y':

    input_string = input("Enter some text : ")

    if len(input_string.split()) == 1:
        modified_input = list(set(input_string))
        print("The occurrences of characters in entered single word are:")

        for iter_char in range(0, len(modified_input)):
            count = 0

            for index in range(0, len(input_string)):
                if modified_input[iter_char] == input_string[index]:
                    count = count + 1

            print("The occurrences of '{}' is {}.".format(modified_input[iter_char], count))

    else:
        temp = input_string.split()
        word_collector = list(set(temp))

        for iter_word in range(0, len(word_collector)):
            count = 0
            for index in range(0, len(temp)):
                if word_collector[iter_word] == temp[index]:
                    count = count + 1

            print("The occurrences of '{}' is {}.".format(word_collector[iter_word], count))

    print("\nDo you want to continue? (Y/N): ", end="")
    flag = input()

# Question 02
# Python program to print next date of input date.

# It must meet following conditions:
#    C1: 1 <= month <= 12
#    C2: 1 <= day <= 30/31
#    C3: 1800 <= year <= 2025

# Collecting data from user.
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

# This block checks for February month and leap year.
if month == 2:

    if (year % 400 == 0) and (year % 100 == 0):
        month_len = 29
    elif (year % 4 == 0) and (year % 100 != 0):
        month_len = 29
    else:
        month_len = 28

# This block checks and then sets the month length to 30 days based on input month.
elif month in [4, 6, 9, 11]:
    month_len = 30

# This block sets the month length to 31 days if above conditions are not executed.
else:
    month_len = 31

if 1 <= day <= month_len and 1 <= month <= 12 and 1800 <= year <= 2025:

    if day == month_len:
        day = 1
        if month == 12:
            # This block will switch to next year.
            month = 1
            year += 1
        else:
            # This block corresponds to last day of month.
            month += 1
    else:
        # This block corresponds to any intermediate day of some month.
        day += 1

    print("Next Date is: ", day, "/", month, "/", year, sep='')

else:
    print("ERROR!! Invalid data entered.The conditions are:")
    print("1 <= day <= 30/31\n1 <= month <= 12\n1800 <= year <= 2025")

# Question 03
# Python program to create a list of tuples with the first element as the
# number and Second element as the square of the number.

input_elements = list()
output_elements = list()

terms = int(input("Enter the number of values to be evaluated: "))

for loop in range(terms):
    input_elements.append(int(input("Enter Number_{} (integer): ".format(loop + 1))))
    output_elements.append((input_elements[loop], input_elements[loop]**2))

print("The inputs given are: ", input_elements)
print("The required output is: ", output_elements)

# Question 04
# Python Program to prompt the user for a grade between 4 and 10. If the grade
# is out of range print error message. If the grade is between 4 and 10 print the
# grade and the performance using the following 'grade_scheme' dictionary variable
# and the required conditions.

flag = 'Y'
grade_scheme = {'A+': 'Outstanding',
                'A': 'Excellent',
                'B+': 'Very Good',
                'B': 'Good',
                'C+': 'Average',
                'C': 'Below Average',
                'D': 'Poor'}

while flag == 'Y':
    grade_points = float(input("Enter the grade points of the student : "))

    while (grade_points <= 3) or (grade_points > 10):
        print("ERROR! The grade points must be an integer from 4 to 10")
        grade_points = float(input("Enter the grade points of the student: "))

    if grade_points == 10:
        print("The student's record: ")
        print("\tYour Grade is '{}' and {} Performance.".format('A+', grade_scheme['A+']))

    elif 9 <= grade_points < 10:
        print("The student's record: ")
        print("\tYour Grade is '{}' and {} Performance.".format('A', grade_scheme['A']))

    elif 8 <= grade_points < 9:
        print("The student's record: ")
        print("\tYour Grade is '{}' and {} Performance.".format('B+', grade_scheme['B+']))

    elif 7 <= grade_points < 8:
        print("The student's record: ")
        print("\tYour Grade is '{}' and {} Performance.".format('B', grade_scheme['B']))

    elif 6 <= grade_points < 7:
        print("The student's record: ")
        print("\tYour Grade is '{}' and {} Performance.".format('C+', grade_scheme['C+']))

    elif 5 <= grade_points < 6:
        print("The student's record: ")
        print("\tYour Grade is '{}' and {} Performance.".format('C', grade_scheme['C']))

    elif 4 <= grade_points < 5:
        print("The student's record: ")
        print("\tYour Grade is '{}' and {} Performance.".format('D', grade_scheme['D']))

    print("\nDo you want to check next Record? (Y/N): ", end='')
    flag = input()

# Question 05
# Python program to print Alphabets Reverse pyramid pattern.

# Brief description:
#    1. The outer for loop is used to count rows.
#    2. The first inner for loop prints the spaces required in each row.
#    3. The second inner for loop prints the letter in required pattern

rows = 6

print("The required pattern is:")

for loop in range(rows):

    for space in range(loop + 5):
        print(" ", end='')

    for letter in range(2*(rows-loop)-1):
        print(chr(65 + letter), end='')

    print()

# Question 06
# Python program to perform some operations on Dictionary.

flag = 'Y'
student_record = list()

while flag == 'Y':

    student_record.append({'SID': int(input("Enter Student ID: ")),
                           'Name': input("Enter Student Name: ")})
    flag = input("Do you want to create a new student record? (Y/N): ")

print("\na.The students details are:")

for loop in range(len(student_record)):
    print(" {}".format(student_record[loop]))

print("\nb.Sorted output using student name:")

# Here x is an arbitrary argument expression variable.
sorted_output = sorted(student_record, key=lambda x: x.get('Name'))
for loop in range(len(sorted_output)):
    print(" {}".format(sorted_output[loop]))

print("\nc.Sorted output using SID:")

# Here y is an arbitrary argument expression variable.
sorted_output = sorted(student_record, key=lambda y: y.get('SID'))
for loop in range(len(sorted_output)):
    print(" {}".format(sorted_output[loop]))

flag = 'Y'

while flag == 'Y':
    print("\nd.Enter the SID for search: ", end='')
    input_SID = int(input())
    search_outcome = 0

    for i in range(len(student_record)):
        if input_SID == student_record[i]['SID']:
            search_outcome = student_record[i]['Name']
            print("The name of the student is:", search_outcome)
            flag = 'N'

    if search_outcome == 0:
        print("ERROR!! SID entered is not there in dictionary.")
        print("Do you want to enter SID again? (Y/N): ", end='')
        flag = input()

# Question 07
# Python program to print Fibonacci sequence also print average of the
# resultant Fibonacci series.

term_1 = 0
term_2 = 1
count = 0
total = 0

terms = int(input("Enter the number of terms: "))

while terms <= 0:
    print("__Enter a positive value__")
    terms = int(input("Enter the number of terms: "))

if terms == 1:
    print("The required Fibonacci sequence is:")
    print(term_1)

else:
    print("The required Fibonacci sequence is:")
    while count < terms:
        print(term_1)

        total = total + term_1

        term_n = term_1 + term_2
        term_1 = term_2
        term_2 = term_n

        count = count + 1

average = total/terms

print("The sum of terms of Fibonacci sequence is: ", total)
print("The average of Fibonacci series: {0:.2f}".format(average))

# Question 08
# Python program to utilize various built-in set methods
# and there corresponding operators.

universal_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}

print("Given set1:", set1)
print("Given set2:", set2)
print("Given set3:", set3, "\n")

set_a = set1 ^ set2
print("a.The set of all elements that are in Set1 and Set2 but not both is:", set_a)

set_b = (set1 | set2 | set3) - (set1 & set2) - (set1 & set2) \
        - (set2 & set3) - (set2 & set3)\
        - (set3 & set1) - (set3 & set1)\
        | (set1 & set2 & set3) | (set1 & set2 & set3) | (set1 & set2 & set3)
print("b.The set of all elements that are in only one of the three sets:", set_b)

set_c = (set1 & set2) | (set2 & set3) | (set3 & set1)\
        - (set1 & set2 & set3) | (set1 & set2 & set3) | (set1 & set2 & set3)
print("c.The set of all elements that are exactly in two of the three sets:", set_c)

set_d = universal_set.difference(set1)
print("d.The set of all integers in the range 1 to 10 that are not in Set1:", set_d)

set_e = universal_set.difference(set1.union(set2, set3))
print("e.The set of all integers in the range 1 to 10 that are not in all three sets:", set_e)
