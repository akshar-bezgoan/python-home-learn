#(b) Write a program that makes the use of trignometric functions available in math module.

import math
 
print('Do you want to use Option 1 - sin, Option 2 - cos or Option 3 - tan?')
print('Enter 1, 2 or 3:')
operation = int(input('--->'))

x = int(input('Enter the number to operate on:'))

if operation == 1: 
	print(math.sin(x))
if operation == 2:
	print(math.cos(x))
else: 
	print(math.tan(x)) 