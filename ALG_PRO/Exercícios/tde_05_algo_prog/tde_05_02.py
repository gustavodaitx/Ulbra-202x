i=int(input("Digite um número Inteiro positivo ( de 1 a 3): "))
a=float(input("Digite um número quaisquer:\n"))
b=float(input("Digite um número quaisquer:\n"))
c=float(input("Digite um número quaisquer:\n"))

lista=[a,b,c]

maior=max(a,b,c)
menor=min(a,b,c)

if i==1:
    lista.sort()
    print(f' Ordem Crescente:{lista}')
    
if i==2:
    lista.sort(reverse=True)
    print(f'Ordem Decrescente:{lista}')
    
elif i==3:
    if(a>b) and (a>c):
        
        print("-="*30)
        print(f'Maior no meio: {b}, {a}, {c}')
    
    if(b>a)and(b>c):
        
        print("-="*30)
        print(f'Maior no meio: {a}, {b}, {c}')
    
    
    if(c>a)and(c>b):
        
        print("-="*30)
        print(f'Maior no meio: {a}, {c}, {b}')

    
    

