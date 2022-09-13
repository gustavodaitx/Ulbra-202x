a=float(input("Digite sua altura: "))
s=input("Digite seu sexo ( masculino ou feminino): ")

if  s=="masculino":
    p1=(72.7*a)-58
    print(f' Seu peso ideal é {p1:.2f} Kg.')
    
if  s=="feminino":
    p2=(62.1*a)-44.7
    print(f' Seu peso ideal é {p2:.2f} Kg.')
