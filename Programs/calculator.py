x = int(input('Enter the number you would like before the sign of operation: '))
print('+ = add - shift & =')
print('- = subtract - press -')
print('* = multiply - shift & 8')
print('/ = divide - fwd slash')
answer = 0
operation_type = input('Enter your math sign you would like to do:  ')
y = int(input('Enter the number you would like after the sign of operation: '))
if operation_type == '+': 
	answer = x + y
if operation_type == '-':
	answer = x - y
if operation_type == '*':
	answer = x * y		
if operation_type == '/': 
	answer = float(x / y)
print(answer)

  
	