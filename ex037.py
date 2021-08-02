import os
from typing import Any

while True:
    AnyNumber = str(input('\n[1] BINARIO\n[2] OCTAL\n[3] HEXADECIMAL\n[4] SAIR\n'))
    
        
    if AnyNumber == '1':
        binario = int(input('digite um numero para converter para binario: '))
        print('seu numero em binário é: ',bin(binario)[2:])
    elif AnyNumber == '2':
        octal = int(input('digite um numero para converter para octal: '))
        print('seu numero em octal é: ',oct(octal)[2:])
    elif AnyNumber == '3':
        hexadecimal = int(input('digite um numero para converter para hexadecimal: '))
        print('seu numero em hexadecimal é: ',hex(hexadecimal)[2:])
    elif AnyNumber == '4':
        exit()