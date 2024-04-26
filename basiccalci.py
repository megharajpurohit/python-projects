a = float(input('Enter value: '))
b = float(input('Enter value: '))
operator = input('Enter the operator: ')

if operator == '+':
    print('Addition is', a + b)
elif operator == '-':
    print('Subtraction is', a - b)
elif operator == '*':
    print('Multiplication is', a * b)
elif operator == '/':
    if b != 0:
        print('Division is', a / b)
    else:
        print('Cannot divide by zero!')
else:
    print('Please enter a valid operator.')