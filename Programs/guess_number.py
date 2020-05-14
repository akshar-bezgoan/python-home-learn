import random 
num = random.randint(1,20)
flag = True 
guess = 2
if guess > 20: exit(); print('Your guess is off limits')
if guess < 1: exit(); print('Your guess is off limits')
print('Guess my number, limit 1 - 20:', end = '')
while flag == True :
  guess = input()
  if not guess.isdigit() :
      print('Invalid! Enter digits only')
      break
  elif int(guess) < num :
       print('Too low, retry:', end = '')
  elif int(guess) > num :
  	   print('Too high, retry:', end = '')
  else: 
    	print('Well Done my number is ' + str(guess))
    	flag = False	  