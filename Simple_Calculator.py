# Simple_Calculator.py
# The zeroth version was taken as the "bad text" from
#   https://www.futurelearn.com/courses/introduction-to-programming-with-python-fourth-rev-/1/steps/1289646
# Then it was made runnable.

# Change 1:  Provide the option to terminate the program to the user
# Notice: this also changes the order of the input:
# Previously, the operands were input fist, and the operation code was input after that.
# Now, the operation coder (or code 0 for termination) was input first.
# If the operation code has been input, then the operands should follow.
# Otherwise, if code 0 was input for termination, then the operands are not read.

# Change 2: Exception handling for when the user gives invalid input for the menu.
# The input should be an integer number from 0 to 4.  If not, an error message is printed,
# and the main menu is displayed again.

# Change 3: Exception handling when the user inputs non-numeric values
# to calculate.
# If a non-numeric number is input, the user is asked to input the number
# again. If a non-numeric number is input again, the flow is returned to the
# main menu. Change: now numbers with decimal point are accepted. Previously,
# the numbers must have been integer.

# Python Program to Make a Simple Calculator

def multiplication(num1, num2):
    return num1 * num2


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def divide_(num1, num2):
    return num1 / num2


def input_number(what_number):
    string = input(f"Enter {what_number}: ")
    try:
        number = float(string)
    except ValueError:
        print("That is not a number. Please input a numeric value.")
        string = input(f"Input {what_number} again: ")
        number = float(string)
    return number


while True:
    print("Enter 0 to quit; or select the operation 1-Division, 2-Multiplication, 3-Addition, 4-Subtraction")
    try:
        operation = int(input("Choose operation 0/1/2/3/4: "))
    except ValueError:
        operation = -1
    if operation == 0:
        break
    if not (0 <= operation < 5):
        print("Not a valid operation code. Enter correct operation, please.")
        operation = -1
        
    if operation > 0:
        try:
            value1 = input_number("1st number")
        except ValueError:
            print("Sorry, that is not a number again. Returning to main menu.")
            operation = -1

    if operation > 0:
        try:
            value2 = input_number("2nd number")
        except ValueError:
            print("Sorry, that is not a number again. Returning to main menu.")
            operation = -1

    # Perhaps, the following block should be also indented. This would make the code more efficient.
    # Not done: reserved for the upcoming changes.
    # As it is now, the code analyser complains that value1 and value2 can be undefined
    if operation == 1:
        print(value1, "/", value2, "=", divide_(value1, value2))
    elif operation == 2:
        print(value1, "*", value2, "=", multiplication(value1, value2))
    elif operation == 3:
        print(value1, "+", value2, "=", addition(value1, value2))
    elif operation == 4:
        print(value1, "-", value2, "=", subtraction(value1, value2))

# The following "else" is unreachable. Commenting it out.
# else:
#     # This line is unreachable, due to the code analyser
#     print("Enter correct operation")
