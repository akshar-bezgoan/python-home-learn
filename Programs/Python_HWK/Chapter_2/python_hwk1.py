#Python Answers

#A -- Answer the following.
#(a) Write a program that swaps the values of variables 'a' and 'b'. You are not allowed to use a 3rd variable. You are not allowed to perform arthimetic on 'a' and 'b'.

print('Enter a number for variable a:')
a = int(input('--->'))
print('Enter another number:')
b = int((input('--->')))
if a > b:
	if b < 0:
		a,b=a-(a-b),b+(a-b)
print(a)
print(b)




#Write a program that generates 5 different numbersin the range 10 to 50. 
from random import randint

for i in range (5) :
	random_num = randint(10,50)
	print(random_num)
	
	















