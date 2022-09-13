n1=float(input("Digite a nota 01 ( 0 a 10):  "))
n2=float(input("Digite a nota 02 ( 0 a 10):  "))
n3=float(input("Digite a nota 03 ( 0 a 10):  "))

ma=(n1+n2+n3)/3

print("-="*30)

print(f'O aluno obteve as notas: {n1}, {n2} e {n3}.')

print("-="*30)

print(f'Sua média de aproveitamento é {ma:.2f}.')

print("-="*30)

if ma>=9.0:
    print("Conceito = A ")
    print("-="*30)
    print(" !!!!A P R O V A D O !!!!  ")
    
elif ma>=7.5 and ma<9.0:
        print("Conceito = B ")
        print("-="*30)
        print(" !!!!A P R O V A D O !!!!  ")
    
elif ma>=6.0 and ma<7.5:
    print("Conceito = C ")
    print("-="*30)
    print(" !!!!A P R O V A D O !!!!  ")
    
elif ma>=4.0 and ma<6.0:
    print("Conceito = D ")
    print("-="*30)
    print(" !!!! REPROVADO !!!!  ")
    
else:
    ma>=9.0
    print("Conceito = E ")
    print("-="*30)
    print(" !!!!REPROVADO!!!!  ")


