a=float(input("Digite um númeor A: \n"))
b=float(input("Digite um númeor B: \n"))
c=float(input("Digite um número C: \n"))

if a>0:
    raiz = float(a)**0.5
    print(f"\n A Raiz quadrada do número {a} é {raiz}\n")
if a<0:
    quad=a**2
    print(f"O quadrado do número {a} é {quad}\n")
    
if c<b:
    dif=b-c
    print(f"A diferença entre {b} e {c} é {dif}\n")
if c>b:
    soma=b+c
    print(f"A Soma entre {b} e {c} é {soma}\n")
    
elif b>10 and b<100:
    print(f"O NÚMERO {b} ESTA ENTRE 10 E 100 - INTERVALO PERMITIDO!!!!")

