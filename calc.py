import time

# Print Welcome message and make the thread sleep for 1 second
print('Welcome to mini Calculator app. Please enter two numbers to get started')
time.sleep(1)

# Take two integer inputs from user
num_1 = int(input('Enter first number (integer only): '))
num_2 = int(input('Enter second number (integer only): '))

# Take operator from user
operator = input('Now select an operator (+ , - , * , / , %) : ').strip()

# Conditional statements to perform correct operations on integers
if operator == '+':
    result = num_1 + num_2
    print('The result of ' + str(num_1) + ' + ' + str(num_2) + ' is ' + str(result))
elif operator == '-':
    result = num_1 - num_2
    print('The result of ' + str(num_1) + ' - ' + str(num_2) + ' is ' + str(result))
elif operator == '*':
    result = num_1 * num_2
    print('The result of ' + str(num_1) + ' * ' + str(num_2) + ' is ' + str(result))
elif operator == '/':
    result = num_1 / num_2
    print('The result of ' + str(num_1) + ' / ' + str(num_2) + ' is ' + str(result))
elif operator == '%':
    result = num_1 % num_2
    print('The result of ' + str(num_1) + ' % ' + str(num_2) + ' is ' + str(result))
else:
    print('Oops! Something went wrong. Please make sure to choose correct operator (+ , - , * , / , %)')