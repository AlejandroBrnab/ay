operation = input("Which operation would you like to do? Choose between addition, substraction, division and multiplication: ")

number1 = int(input("First number: "))
number2 = int(input("Second number: "))

result = 0

if operation == "addittion":
    result = number1 + number2

if operation == "substraction":
    result = number1 - number2

if operation == "division":
    result = number1 / number2

if operation == "multiplication":
    result = number1 * number2

print(result)