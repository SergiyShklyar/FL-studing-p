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

# Python Program to Make a Simple Calculator

def multiplication(num1, num2):
    return num1 * num2


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def divide_(num1, num2):
    return num1 / num2


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
        value1 = int(input("Enter 1st number: "))
        value2 = int(input("Enter 2nd number: "))
  
    # These were put into the body of IF-statement due to the complaints of the code analyser.
        if operation == 1:
            print(value1, "/", value2, "=", divide_(value1, value2))
        elif operation == 2:
            print(value1, "*", value2, "=", multiplication(value1, value2))
        elif operation == 3:
            print(value1, "+", value2, "=", addition(value1, value2))
        elif operation == 4:
            print(value1, "-", value2, "=", subtraction(value1, value2))
