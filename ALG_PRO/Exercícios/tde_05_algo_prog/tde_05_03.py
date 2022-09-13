print("Índices de Poluição: 0.025 a 0.25 = Aceitáveis !!!\n")
print("Índices de Poluição: 0.25 a 0.4 =Primeiro Grupo deve suspender suas atividades!!\n")
print("Índices de Poluição: 0.4 a 0.5 = Grupos 01 e 02 deverão ser notificados !!\n")
print("Índices de Poluição: maior que 0.5= Os 03 Grupos deverão ser notificados\n")


indice=float(input("Qual o Índice de Poluição: "))

if indice>=0.025 and indice<=0.25:
        
        print(f'O índice de Poluição está Aceitável!!')
    
if indice>0.25 and indice<0.4:
        
        print(f'Primeiro Grupo deve suspender suas atividades!!')

elif indice>=0.4 and indice<0.5:
        
        print(f'Grupos 01 e 02 deverão ser notificados !!')

if indice>=0.5:
        
        print('Os 03 Grupos deverão ser notificados!!!')