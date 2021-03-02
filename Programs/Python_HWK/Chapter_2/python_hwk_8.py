
def complex_destructuriser() :
	x = int(input('Enter a number for a complex number: '))
	y = float(input('Enter another number: '))
	z = complex(x,y)
	print(f'For the complex number {z} the real number is {z.real}, the imaginary number is {z.imag} and the conjugate is {z.conjugate}.')
	a = complex(y,x)
	print(f'Or Vice Versa for {a}, the real number is {a.real}, the imaginary number is {a.imag} and the conjugate is {a.conjugate}.')

complex_destructuriser()

