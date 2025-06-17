#add
def add(x, y):
    return x + y
#sub
def subtract(x, y):
    return x - y
#mul
def multiply(x, y):
    return x * y 
#devition
def divide(x, y):
    return x / y
#mod
def modulus(x, y):
    return x % y
#square root
def square_root(x):
    if x < 0:
        return "Error! Cannot calculate square root of a negative number."
    return x ** 0.5

def calculator():
    print("select operation")
    print(" 1 for Add \n 2 for sub \n 3 for multiply \n 4 for divide \n 5 for modulus \n 6 for square root")
    while True:
        operation = input("selected operation: ")
        
        if operation.isdigit():
            operation = int(operation) 
            if(operation>=7):
                print("only values from 1 to 6 are allowed")
                continue
#ADD            
            elif(operation == 1):
                firstNumber=(input("Enter First Number: "))
                secondNumber=(input("Enter second Number: "))
                if (firstNumber.isdigit() and secondNumber.isdigit()):
                    firstNumber = int(firstNumber)
                    secondNumber = int(secondNumber)
                    print("the result is: ")
                    print (f"{firstNumber} + {secondNumber} = {add (firstNumber , secondNumber)  }")
                    break
                else:
                    print ("only positive numbers")
                    continue
#sub
            elif(operation == 2):
                firstNumber=(input("Enter First Number: "))
                secondNumber=(input("Enter second Number: "))
                if (firstNumber.isdigit() and secondNumber.isdigit()):
                    firstNumber = int(firstNumber)
                    secondNumber = int(secondNumber)
                    print("the result is: ")
                    print (f"{firstNumber} - {secondNumber} = {subtract (firstNumber , secondNumber)  }")
                    break
                else:
                    print ("only positive numbers")
                    continue

#mul
            elif(operation == 3):
                firstNumber=(input("Enter First Number: "))
                secondNumber=(input("Enter second Number: "))
                if (firstNumber.isdigit() and secondNumber.isdigit()):
                    firstNumber = int(firstNumber)
                    secondNumber = int(secondNumber)
                    print("the result is: ")
                    print (f"{firstNumber} * {secondNumber} = {multiply (firstNumber , secondNumber)  }")
                    break
                else:
                    print ("only positive numbers")
                    continue 

#div
            elif(operation == 4):
                firstNumber=(input("Enter First Number: "))
                secondNumber=(input("Enter second Number: "))
                if (firstNumber.isdigit() and secondNumber.isdigit()):
                    firstNumber = int(firstNumber)
                    secondNumber = int(secondNumber)
                    
                    if secondNumber != 0:
                        print("the result is: ")
                        print (f"{firstNumber} / {secondNumber} = {divide (firstNumber , secondNumber)  }")
                        break
                    else:
                        print ("0 cant be a denominator")
                        continue
                else:
                    print ("only positive numbers")
                    continue
#mod
            elif(operation == 5):
                firstNumber=(input("Enter First Number: "))
                secondNumber=(input("Enter second Number: "))
                if (firstNumber.isdigit() and secondNumber.isdigit()):
                    firstNumber = int(firstNumber)
                    secondNumber = int(secondNumber)
                    
                    if secondNumber == 0:
                        print("Error: Division or modulus by zero is not allowed.")
                        continue
                    print("the result is: ")
                    print (f"{firstNumber} % {secondNumber} = {modulus (firstNumber , secondNumber)  }")
                    break
                else:
                    print ("only positive numbers")
                    continue

#square root
            elif(operation == 6):
                number = input("Enter a number to find its square root: ")
                if number.isdigit():
                    number = int(number)
                    result = square_root(number)
                    print("the result is: ")
                    print(f"The square root of {number} is {result}")
                    break
                else:
                    print("Please enter a valid positive number.")
                    continue
        else:
            print("input numbers only")
            continue
#continue or end
    while True:
        continue_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if continue_calculation == 'yes':
            calculator()
            break
        elif continue_calculation == 'no':
            print("Thank you for using the calculator!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
        
calculator()

#explanations