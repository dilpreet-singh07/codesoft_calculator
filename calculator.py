user_input = float(input("Enter number1:"))
other_input = float(input("Enter number2:"))
choice = print("Your choices are '+','-','*','/','%'")
choice_input = input("Enter your choice:")
cntinu = True
while cntinu:
    if choice_input == '+':
        result = user_input + other_input
        print(f"The result is {result}")
    elif choice_input == '-':
        result = user_input - other_input
        print(f"The result is {result}")
    elif choice_input == '*':
        result = user_input * other_input
        print(f"The result is {result}")
    elif choice_input == '/':
        result = user_input / other_input
        print(f"The result is {result}")
    elif choice_input == '%':
        result = user_input % other_input
        print(f"The result is {result}")
    else:
        print("You entered something wrong")
    cntinu_input = input("Do you want to continue?'yes' or 'no'").lower()
    if cntinu_input == 'no':
        cntinu = False
        print("Thanks for using the calculator")
