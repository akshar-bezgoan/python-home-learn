
prediction_year = int(raw_input( 'Enter the year you want to know your age in:'))
if prediction_year < 2020: print('Invalid Response'); exit()
print('Enter accordingly for birth month')
print ('1 = January')
print ('2 = February')
print ('3 = March')
print ('4 = April') 	
print ('5 = May	')
print ('6 = June')
print ('7 = July')
print ('8 = August')
print ('9 = September')
print ('10 = October')
print ('11 = November') 
print ('12 = December') 	
prediction_month = int (raw_input( 'Enter the month you want to know your age in:'))
if prediction_month > 12: print('Invalid Response'); exit()
if prediction_month < 0: print('Invalid Response'); exit()
DOB_year = int(raw_input( 'Enter the year you were born in:' )) 
if DOB_year > 2020:print('Invalid Response'); exit()
DOB_month = int(raw_input( 'Enter the month you were born in:'))
if DOB_month > 12:print('Invalid Response'); exit()
if DOB_month < 0: print('Invalid Response'); exit()
prediction_age = prediction_year - DOB_year
print (('You will be ') + str(prediction_age) + ' in ' + str(prediction_year))
if prediction_month < DOB_month: 
		prediction_age = prediction_age - 1 

