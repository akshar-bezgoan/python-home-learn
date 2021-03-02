def gross_salary_calc() :
	x = int(input('Enter Rameshs basic salary: '))
	currency = input('Enter the currency: ')
	gross_salary = x-(x*0.4)-(x*0.2)
	print(f'Rameshs gross salary is {currency} {gross_salary}.')
gross_salary_calc()