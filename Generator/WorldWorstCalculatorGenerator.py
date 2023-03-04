with open('WorldWorstCalculator.py', 'w') as arquivo:
    arquivo.write('firstNumber = int(input("Enter the first number: "))\n')
    arquivo.write('operator = input("Enter the operator (+, -, /, *): ")\n')
    arquivo.write('secondNumber = int(input("Enter the second number: "))\n')
    arquivo.write('result = None\n')


    arquivo.write('\n# Addition\n\n')
    for i in range(101):
        for j in range(101):
            arquivo.write("result = " + str(i+j) + " if firstNumber == " + str(i) + " and operator == '+' and secondNumber == " + str(j) + " else result\n")

    arquivo.write('\n# Subtraction\n\n')
    for i in range(101):
        for j in range(101):
            arquivo.write("result = " + str(i-j) + " if firstNumber == " + str(i) + " and operator == '-' and secondNumber == " + str(j) + " else result\n")

    arquivo.write('\n# Division\n\n')
    for i in range(1, 101):
        for j in range(1, 101):
            arquivo.write("result = " + str(i/j) + " if firstNumber == " + str(i) + " and operator == '/' and secondNumber == " + str(j) + " else result\n")

    arquivo.write('\n# Multiplication\n\n')
    for i in range(101):
        for j in range(101):
            arquivo.write("result = " + str(i*j) + " if firstNumber == " + str(i) + " and operator == '*' and secondNumber == " + str(j) + " else result\n")


    arquivo.write('\nif result is not None:\n')
    arquivo.write('    print("The result is:", result)\n')
    arquivo.write('else:\n')
    arquivo.write('    print("The requested operation is invalid.")\n')
