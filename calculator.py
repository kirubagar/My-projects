


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


def stop():
    user_input = input("type 'y' for continue calculation or 'n' to end calculation ")
    if user_input == "y":
        calculator()
    elif user_input == "n":
        quit()
    else:
        print("invalid input")


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}
from art import logo
print(logo)
def calculator():
    continue_calculating = True
    first_input = int(input(f"please type the first number "))
    while continue_calculating:
        for symbols in operations:
            print(symbols)
        second_input = input("pick your choice of operation ")
        third_input = int(input(f"please type the second number "))

        if second_input in operations:
            result = operations[second_input](first_input, third_input)
            print(f"{first_input} {second_input} {third_input} = {result}")

            fourth_input = input(f"type 'yes' if you wants to continue working with the previous result {result} and 'no' to end ")

            if fourth_input.lower() == "yes":
                first_input = result
            elif fourth_input.lower() == "no":
                continue_calculating = False
                print("\n" * 20)
                stop()

        else:
            print("invalid operation")


calculator()