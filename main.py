# Define the functions
def add(num1,num2):
  result = num1 + num2
  print(str(num1) + " " + "+" + " " + str(num2) + " " + "=" + " " +  str(result))

def sub(num1,num2):
  result = num1 - num2
  print(str(num1) + " " + "-" + " " + str(num2) + " " + "=" + " " + str(result))

def mul(num1,num2):
  result = num1 * num2
  print(str(num1) + "*" + str(num2) + " " + "=" + " " + str(result))

def div(num1,num2):
  result = num1 / num2
  print(str(num1) + "/" + str(num2) + " " + "=" + " " + str(result))

def expo(num1, num2):
  result = num1 ** num2
  print(str(num1) + "^" + str(num2) + " " + "=" + " " + str(result))

# Prints the options for the user and prompts the user to choose an option
print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Divisiion")
print("E. Exponentiation")
print("F. Exit")

option = input("Input an option: ")

# Conditonal statements to evaluate user's choice and function call
if option == "a" or option == "A":
    print("Addition")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    add(num1,num2)
elif option == "b" or option == "B":
    print("Subtraction")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    sub(num1,num2)
elif option == "c" or option == "C":
    print("Multiplication")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    mul(num1,num2)
elif option == "d" or option == "D":
    print("Division")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    div(num1,num2)
elif option == "e" or option == "E":
    print("Exponentation")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    expo(num1,num2)
elif option == "f" or option == "F":
    print("End of program")
    quit()