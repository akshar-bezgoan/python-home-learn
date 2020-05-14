
print('Think of the number of the month you were born in')
input('press return.....')
print('Double that number')
input('press return.....')
print('Then add 5')
input('press return.....')
print('Then multiply it by 5')
input('press return.....')
print('Then multiply it by 10')
input('press return.....')
dob_predict = int(input('Then add your date to the number for e.g. if you are born on the 19th of March add 19 and type it here '))
answer = dob_predict - 250
month = (int)(answer / 100)
date = (int) (answer %100)
print('Your were born on ' + str(date) + '/' + str(month))  


