# QUESTION 01
# Python script to make a GUI-based GST Tax Finder Calculator which takes
# original cost and net price as an input from the user and display the GST result.

from tkinter import *


def calculate_gst():

    # Accepting the input from Entry widget
    # using the get method.

    original_cost = int(or_cost_field.get())
    net_cost = int(net_price_field.get())

    # Checking whether net price is less than original price.

    if net_cost < original_cost:
        gst_result_field.insert(10, "ERROR!!")

    else:
        # GST Calculation formula used.

        gst_rate = ((net_cost - original_cost) * 100) / original_cost

        # Using the insert method to display
        # the output in Entry widget.

        gst_result_field.insert(10, str('%.2f' % gst_rate) + " % ")


def clear_data():

    # Creating this function to
    # clear the contents of all
    # the entry widgets.

    or_cost_field.delete(0, END)

    net_price_field.delete(0, END)

    gst_result_field.delete(0, END)


if __name__ == '__main__':

    # Creating a root window.
    # Configure the root window by
    # setting geometry, background color and title.

    win = Tk()
    win.geometry("430x350")

    # To fix the size of GUI window uncomment below lines
    # win.minsize(450, 350)
    # win.maxsize(450, 350)

    win.title("GST Tax Finder Calculator")
    win.configure(background="#333333")

    # Creating Labels for:
    # 1. heading
    # 2. Original Cost as or_cost
    # 3. Net Price as net_price
    # 4. GST Rate as gst_result

    heading = Label(win, text="Welcome to GST Tax Finder Calculator,\n "
                              "Calculate your GST Rate.", bg="#333333", font="Impact 15", fg="white", padx=5, pady=5)

    or_cost = Label(win, text="Original Cost", bg="#003152", fg="white", padx=5, pady=5)

    net_price = Label(win, text="Net Price", bg="#003152", fg="white", padx=5, pady=5)

    gst_result = Label(win, text="GST Rate", bg="#003152", fg="white", padx=5, pady=5)

    # Placing the Label widget using the
    # grid method.

    heading.grid(row=0, column=0, columnspan=2, sticky='ew', padx=10, pady=10)

    or_cost.grid(row=1, column=0,  sticky='ew', padx=10, pady=10)

    net_price.grid(row=2, column=0,  sticky='ew', padx=10, pady=10)

    gst_result.grid(row=3, column=0,  sticky='ew', padx=10,  pady=10)

    # Creating the required entry box fox taking
    # inputs and displaying outputs.

    or_cost_field = Entry(win, width=50)

    net_price_field = Entry(win, width=50)

    gst_result_field = Entry(win, width=50)

    # Placing the Entry widget using the
    # grid method

    or_cost_field.grid(row=1, column=1,  padx=10, pady=10)

    net_price_field.grid(row=2, column=1, padx=10, pady=10)

    gst_result_field.grid(row=3, column=1,  padx=10, pady=10)

    # Creating some Buttons as:
    # 1. Button to calculate GST
    #    using calculate_gst function.
    # 2. Button to clear the inputs and outputs
    #    using clear_data function.

    Button(win, text="Calculate GST", fg="white", bg="#004242",
           command=calculate_gst, padx=10, pady=10).grid(row=4, column=1,  columnspan=2, sticky='ew', padx=10, pady=10)

    Button(win, text="Clear DATA", fg="white", bg="#004242",
           command=clear_data, padx=10, pady=10).grid(row=5, column=1, columnspan=2, sticky='ew', padx=10, pady=10)

    win.mainloop()

# QUESTION 02
# A Python program to create a GUI-based Calendar application using Tkinter module
# that display the calendar with respect to the year entered by the user.

from tkinter import *
import calendar
import tkinter.messagebox as tmsg


def show_calendar():

    if int(year_field.get()) <= 0:
        tmsg.showinfo("ERROR !", "The year cannot be negative or zero. Enter a valid year.")
        return

    # Creating a sub window.
    # Configure the sub window by
    # setting geometry, background color and title.

    sub = Tk()
    sub.geometry("550x590")
    sub.minsize(550, 590)
    sub.maxsize(550, 590)
    sub.config(background="white")
    sub.title("Calendar Of The YEAR: " + year_field.get())

    fetch_year = int(year_field.get())

    # Using calendar method of calendar module to get
    # the calendar of the input year.

    calendar_fetched = calendar.calendar(fetch_year)

    # Creating a label for showing the fetched calendar.

    calendar_year = Label(sub, text=calendar_fetched, bg="#2B6974", fg="white", font="Consolas 10 bold")

    # Using the grid method for placing
    # the widget at required location.

    calendar_year.grid(row=5, column=1, padx=20)

    sub.mainloop()


if __name__ == '__main__':

    # Creating a root window.
    # Configure the root window by
    # setting geometry, background color and title.

    root = Tk()
    root.geometry("300x200")
    root.minsize(300, 200)
    root.maxsize(300, 200)
    root.title("MY CALENDAR")
    root.config(background="#008080")

    # Creating the necessary Labels and Buttons for the required GUI application.

    calendar_label = Label(root, text="MY CALENDAR", bg="#008080", fg="white",
                font=("Bradley Hand ITC", 28, 'bold'))

    year_label = Label(root, text="Type a Year", font=("Arial", 15, 'bold'), bg="#008080", fg="#333333")

    year_field = Entry(root)

    show_button = Button(root, text="Display Calendar", fg="#000000",
                  bg="#aabbf0", padx=5, pady=5, font="Arial 10 bold", borderwidth=6, command=show_calendar)

    exit_button = Button(root, text="Exit Calendar Application", fg="#000000",
                  bg="#ff4860", padx=5, pady=5, font="Arial 10 bold", borderwidth=6, command=exit)

    # Using the grid method for placing
    # the widgets at required locations.

    calendar_label.grid(row=1, column=1)
    year_label.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    show_button.grid(row=4, column=1, pady=5)
    exit_button.grid(row=6, column=1)

    root.mainloop()

# QUESTION 03
# A Python script to create a GUI-based calculator using Tkinter module, which can
# perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

from tkinter import *
from tkinter import font as tkFont


# Declaring a variable globally
var_expression = ""


def press(symbol):

    global var_expression

    var_expression = var_expression + str(symbol)

    # Updating the var_expression by using set method
    display.set(var_expression)

# Creating a function to formulate the required
# operation.


def get_result():

    # Here, try and except statement is used
    # for handling the errors.

    try:

        global var_expression

        # eval function evaluate the expression
        # and str function convert the result
        # into string

        output = str(eval(var_expression))

        display.set(output)

        # initialize the expression variable
        # by empty string

        var_expression = ""

    # if error is generated then handle
    # by the except block

    except:

        display.set("ERROR")
        var_expression = ""


# Creating a clear function to delete the contents
# of text entry box.

def clear():

    global var_expression

    var_expression = ""

    display.set("")

if __name__ == "__main__":

    # Creating a root window.
    # Configure the root window by
    # setting geometry, background color and title.

    root = Tk()
    root.geometry("350x500")
    root.minsize(350, 500)
    root.maxsize(350, 500)
    root.configure(background="#F5F5F5")
    root.title("Basic Calculator")

    # Creating a title Label as Calculator.

    heading = Label(root, text="Calculator", bg="#F5F5F5", font=('Vani', 20))
    heading.grid(row=0, column=0, sticky='w', padx=10, pady=10)

    # Creating the instance of StringVar() Class of Tkinter.

    display = StringVar()
    expression_field = Entry(root, width=9, textvariable=display, highlightthickness=1,
                             highlightcolor="#000000", bg="#F5F5F5", font=('Arial', 50))
    expression_field.grid(row=1, column=0, sticky='EWNS', padx=5, pady=10)

    # Creating the required buttons and attaching
    # them with suitable functions.

    f1 = Frame(root, bg="#F5F5F5")
    f1.grid(row=2, column=0,rowspan=5, columnspan=5, sticky='EWNS', padx= 12, pady=10)

    button_font = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD)

    button_1 = Button(f1, text=' 1 ', fg='black', bg='white', font=button_font, activebackground="#87ceeb",
                     command=lambda: press(1), height=2, width=6)
    button_1.grid(row=2, column=0)

    button_2 = Button(f1, text=' 2 ', fg='black', bg='white', font=button_font, activebackground="#87ceeb",
                     command=lambda: press(2), height=2, width=6)
    button_2.grid(row=2, column=1)

    button_3 = Button(f1, text=' 3 ', fg='black', bg='white', font=button_font, activebackground="#87ceeb",
                     command=lambda: press(3), height=2, width=6)
    button_3.grid(row=2, column=2)

    button_4 = Button(f1, text=' 4 ', fg='black', bg='white', font=button_font, activebackground="#87ceeb",
                     command=lambda: press(4), height=2, width=6)
    button_4.grid(row=1, column=0)

    button_5 = Button(f1, text=' 5 ', fg='black', bg='white', font=button_font, activebackground="#87ceeb",
                     command=lambda: press(5), height=2, width=6)
    button_5.grid(row=1, column=1)

    button_6 = Button(f1, text=' 6 ', fg='black', bg='white',font=button_font, activebackground="#87ceeb",
                     command=lambda: press(6), height=2, width=6)
    button_6.grid(row=1, column=2)

    button_7 = Button(f1, text=' 7 ', fg='black', bg='white', font=button_font, activebackground="#87ceeb",
                     command=lambda: press(7), height=2, width=6)
    button_7.grid(row=0, column=0)

    button_8 = Button(f1, text=' 8 ', fg='black', bg='white', font=button_font, activebackground="#87ceeb",
                     command=lambda: press(8), height=2, width=6)
    button_8.grid(row=0, column=1)

    button_9 = Button(f1, text=' 9 ', fg='black', bg='white', font=button_font, activebackground="#87ceeb",
                     command=lambda: press(9), height=2, width=6)
    button_9.grid(row=0, column=2)

    button_0 = Button(f1, text=' 0 ', fg='black', bg='white', font=button_font, activebackground="#87ceeb",
                     command=lambda: press(0), height=2, width=6)
    button_0.grid(row=3, column=1)

    plus_button = Button(f1, text=' + ', fg='black', bg='white', font=button_font, activebackground="#87ceeb",
                  command=lambda: press("+"), height=2, width=6)
    plus_button.grid(row=3, column=4)

    minus_button = Button(f1, text=' - ', fg='black', bg='white', font=button_font, activebackground="#87ceeb",
                   command=lambda: press("-"), height=2, width=6)
    minus_button.grid(row=2, column=4)

    multiply_button = Button(f1, text=' * ', fg='black', bg='white', font=button_font, activebackground="#87ceeb",
                      command=lambda: press("*"), height=2, width=6)
    multiply_button.grid(row=1, column=4)

    divide_button = Button(f1, text=' / ', fg='black', bg='white', font=button_font, activebackground="#87ceeb",
                    command=lambda: press("/"), height=2, width=6)
    divide_button.grid(row=0, column=4)

    equal_button = Button(f1, text=' = ', fg='black', bg="#1E90FF", font=button_font, activebackground="#87ceeb",
                   command=get_result, height=2, width=6)
    equal_button.grid(row=3, column=2)

    clear_button = Button(f1, text='Clear', fg='black', bg='white',font=button_font, activebackground="#87ceeb",
                   command=clear, height=2, width=5)
    clear_button.grid(row=6, column=0, columnspan=5, sticky="ew")

    decimal_button = Button(f1, text='.', fg='black', bg='white',font=button_font, activebackground="#87ceeb",
                    command=lambda: press('.'), height=2, width=6)
    decimal_button.grid(row=3, column=0)

    root.mainloop()

# QUESTION 04
# A Python Program to create a list of marks for n number of students entered by the user.
# Sort the input list using merge/Quick sort algorithm and print the final sorted List.
# Here I have used Merge Sort Algorithm to sort the list.


def merge_sort(data):
    # This function defines the Merge Sort algorithm to be performed on
    # the students marks list.
        
    if len(data) > 1:

        # mid is the point where the list is divided into two sub lists.
        mid = len(data)//2
        left_list = data[:mid]
        right_list = data[mid:]

        # Calling merge_sort function again to sort the two sub lists.
        merge_sort(left_list)
        merge_sort(right_list)

        # Setting three pointers one for each of the two sub lists
        # and one for maintaining the current index of the corresponding
        # final sorted list. Initializing all three pointer to zero value.
        i = j = k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                data[k] = left_list[i]
                i += 1
            else:
                data[k] = right_list[j]
                j += 1
            k += 1

        # Copying the elements of other sub list into corresponding
        # final sorted list when any one of
        # the sub list is exhausted/completed.
        while i < len(left_list):
            data[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            data[k] = right_list[j]
            j += 1
            k += 1


if __name__ == '__main__':

    marks = []
    total_students = int(input("Enter the number of students: "))

    print("Enter the marks of students in this Subject:")

    for loop in range(0, total_students):
        marks.append(int(input(f"Enter marks of STUDENT {loop + 1}: ")))

    print("Marks list entered by the user:", marks)

    merge_sort(marks)

    print("Marks after required sorting:", marks)

# QUESTION 05
# A Python Program to create an integer array containing duplicates entered by the user
# and then perform certain sorting, searching and counting operations.


def partition(data, low, high):
    # This function performs and find the partition position
    # to fix the final position of pivot(reference) element.

    # Selecting the rightmost element of the data
    # as the reference element.
    pivot = data[high]

    # Setting up a pointer for element greater than the pivot
    i = low - 1

    # Comparing each element pointed by j in data with pivot.
    for j in range(low, high):
        if data[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # The return from the function is the positio where partition is done.
    return i + 1


def quick_sort(data, low, high):
    # This function perform Quick Sort algorithm.

    if low < high:
        # Searching for the final position of pivot(reference)
        # element such that elements smaller than pivot are on the left
        # and elements greater than pivot are on the right.
        pivot_index = partition(data, low, high)

        # Applying quicksort on the left sub list of the final
        # position of pivot recursively.
        quick_sort(array, low, pivot_index - 1)

        # Applying quick sort on the right sub list of the final
        # position of pivot recursively.
        quick_sort(array, pivot_index + 1, high)


def binary_search(data, number, low, high, flag):
    result = -1

    while low <= high:

        mid = (low + high)//2

        if data[mid] == number:
            result = mid
            if flag:
                high = mid - 1
            else:
                low = mid + 1

        elif data[mid] < number:
            low = mid + 1

        else:
            high = mid - 1

    return result


if __name__ == '__main__':

    array = []
    array_length = int(input("Enter the length of array: "))

    print("Enter only integer values:")

    for loop in range(0, array_length):
        array.append(int(input(f"Enter INTEGER {loop + 1}: ")))

    print("The Input Array:", array)

    quick_sort(array, 0, array_length-1)

    print("\na. The Sorted Array:", array)

    num = int(input("\nb. Enter the integer value to search for: "))

    first_index = binary_search(array, num, 0, array_length-1, True)

    if first_index == -1:
        print(f"ERROR! The element {num} is not present in the list.")
        print(f"\nc. The number of occurrences of element {num} is:", 0)

    else:
        last_index = binary_search(array, num, 0, array_length-1, False)

        print(f"The element {num} is present in the Sorted Array at indices:")

        for loop in range(first_index, last_index+1):
            print(f"\t{loop}")

        print(f"\nc. The number of occurrences of element {num} is:", last_index-first_index+1)

