def xor(x, y):
    xored = []
    for i in range(1, len(y)):
        if x[i] == y[i]:
            xored.append('0')
        else:
            xored.append('1')
    return ''.join(xored)
def division(divident, divisor):
    divisor_bits = len(divisor)
    var = divident[0: divisor_bits]
    while divisor_bits < len(divident):
        if var[0] == '1':
            var = xor(divisor, var) + divident[divisor_bits]
        else:
            var = xor('0' * divisor_bits, var) + divident[divisor_bits]
        divisor_bits += 1
    if var[0] == '1':
        var = xor(divisor, var)
    else:
        var = xor('0' * divisor_bits, var)
    crc = var
    return crc
def transmit_data(data, key):
    divisor_bits = len(key)
    add_data = data + '0'*(divisor_bits-1)
    remainder = division(add_data, key)
    transmitted_frame = data + remainder
    print("Remainder : ", remainder)
    print("The transmitted Codeword(Data + CRC) is : ", transmitted_frame)
def receiver(data, key):
    print(f'The received code word contains no errors as the remainder is{division(data, key)}.')
    data_bit = input('Enter the n-bit data stream = ')
    degree = int(input('What is the degree of the polynomial = '))
    polynomial = ''
    for i in reversed(range(-1, degree)):
        bit = input(f'Enter the Coefficient of x^{i + 1} = ')
        polynomial = polynomial + bit
    transmit_data(data_bit, polynomial)
    receiver(input('Please enter the received Code Word: '), polynomial)
