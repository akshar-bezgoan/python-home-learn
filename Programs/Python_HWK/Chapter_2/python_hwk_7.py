fahrenheit = float(input('Enter a temperature in Fahrenheit and you will recieve it as Celsius, dont include Fahrenheit at the end:  '))
celsius = format((fahrenheit - 32)*(5/9),'0.2f')
print(f'{celsius} degrees Celsius')
