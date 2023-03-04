# World Worst Calculator
 The calculator made in the WORST possible way.

# How it works?
The calculator uses a series of hard-coded examples in if statements to perform the calculation. For example, if the operator is "+", the calculator checks the value of firstNumber and secondNumber, and sets the result variable to the correct answer based on the inputs.
In this example, the program only supports values up to 100 in order to keep it "runnable".

# How did you do that?
I wrote the Python file WorldWorstCalculatorGenerator.py (in the Generator folder) to create the calculator. It uses nested for-loops to generate a series of if-statements for each possible combination of numbers and operators. For each combination, the appropriate result is assigned to the result variable.

If you want to go on an adventure to make this calculator even worse (or maybe better?), all you have to do is adjust the range in the generator for loops. You can increase the range to support more values, but the file size will become significantly larger and the program will take longer to run.