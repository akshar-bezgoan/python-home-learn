
def binary_to_decimal():
    binary = input('Enter a binary number: ')
    i,integer = 0,0
    size = len(binary)
    while i < len(binary):
        integer += int(binary[size - 1 - i])*pow(2,i)
        i+=1
    print(f'Your Decimal value is {integer}.')
binary_to_decimal()