# Task 1: Understanding Python Exceptions
def task1():
    while True:

        # ZeroDivisionError and ValueError Example
        try:
            number = int(input("Enter a number: "))
            result = 100 / number
        except ZeroDivisionError:
            print("Oops, you cannot divide by zero.")
        except ValueError:
            print("Invalid input, please enter a valid number.")
        else:
            print(f"100 divided by {number} is {result}")
            break

# Task 2: Types of Exceptions
def task2():

    # IndexError Example
    try:
        new_list = [1, 2, 3]
        print(new_list[5])
    except IndexError:
        print("IndexError occured, requested list index is out of range.")
        
    # KeyError Example
    try:
        new_dict = {
            "name": "Andre"
        }
        print(new_dict["age"])
    except KeyError:
        print("KeyError occured, the key does not exist in the dictionary.")

    # TypeError Example
    try:
        result = "abc" + 123
    except TypeError:
        print("TypeError occured, cannot concatenate string and integer.")

# Task 3: Using Try-Except-Else-Finally
def task3():
    try:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        result = number1/ number2
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError:
        print("Invalid input, please enter a valid number.")
    else:
        print(f"The result of {number1} divided by {number2} is {result}")
    finally:
        print("Execution completed. (This block will always run)")

# Execute the tasks (main menu)
def main_menu():
    while True:
        print("\nPython Error Handling Menu")
        print("1. Task 1 - Understanding Python Exceptions")
        print("2. Task 2 - Types of Exceptions")
        print("3. Task 3 - Try-Except-Else-Finally")
        print("4. Exit")

        choice = input("Choose a task (1-4): ")

        if choice == '1':
            print("\nRunning Task 1:")
            task1()
        elif choice == '2':
            print("\nRunning Task 2:")
            task2()
        elif choice == '3':
            print("\nRunning Task 3:")
            task3()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Start the program
main_menu()