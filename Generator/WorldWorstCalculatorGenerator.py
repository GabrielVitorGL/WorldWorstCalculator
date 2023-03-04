with open('../WorldWorstCalculator.py', 'w') as file:
    file.write('firstNumber = int(input("Enter the first number: "))\n')
    file.write('operator = input("Enter the operator (+, -, /, *): ")\n')
    file.write('secondNumber = int(input("Enter the second number: "))\n')
    file.write('result = None\n')


    file.write('\n# Addition\n\n')
    for i in range(101):
        for j in range(101):
            file.write("result = " + str(i+j) + " if firstNumber == " + str(i) + " and operator == '+' and secondNumber == " + str(j) + " else result\n")

    file.write('\n# Subtraction\n\n')
    for i in range(101):
        for j in range(101):
            file.write("result = " + str(i-j) + " if firstNumber == " + str(i) + " and operator == '-' and secondNumber == " + str(j) + " else result\n")

    file.write('\n# Division\n\n')
    for i in range(1, 101):
        for j in range(1, 101):
            file.write("result = " + str(i/j) + " if firstNumber == " + str(i) + " and operator == '/' and secondNumber == " + str(j) + " else result\n")

    file.write('\n# Multiplication\n\n')
    for i in range(101):
        for j in range(101):
            file.write("result = " + str(i*j) + " if firstNumber == " + str(i) + " and operator == '*' and secondNumber == " + str(j) + " else result\n")


    file.write('\nif result is not None:\n')
    file.write('    print("The result is:", result)\n')
    file.write('else:\n')
    file.write('    print("The requested operation is invalid.")\n')
