distance = int(input('Enter a distance (in km) without the km at the end: '))
metre = distance/1000
foot = distance/3280.8399
inch = distance/39370.0787
centimetre = distance/100000 
def metric_conversion(distance ,metre ,foot ,inch ,centimetre) :
	print(f'Your distance in metres is {metre}')
	print(f'Your distance in feet is {foot}')
	print(f'Your distance in inches is {inch}')
	print(f'Your distance in centimetres is {centimetre}')
metric_conversion(distance ,metre ,foot ,inch ,centimetre)	
	
