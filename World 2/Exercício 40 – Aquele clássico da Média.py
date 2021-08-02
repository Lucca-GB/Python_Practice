nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
notaFinal = (nota1 + nota2) / 2

if(notaFinal < 5):
    print(" \nREPROVADO!\n")
elif(7 > notaFinal >= 5):
    print(" \nRECUPERAÇÃO! \n")
elif(notaFinal >= 7):
    print(" \nAPROVADO! \n")
