nota_ps=float(input("Digite sua nota: "))

if nota_ps>=6:
    print("Você foi aprovado\n")
    print("Parabéns\n")
    if nota_ps>9:
        print("Você é D+")
elif nota_ps<6 and nota_ps>4:
    print("Você ficou em exame")
    print("Sem pizza pra turma")
else:
    
    print("Você não foi aprovado")
    
print(f"sua nota é {nota_ps}")

if not False:
    print("Isto é Verdade!!")
else:
    print("Isso é Falso!!")
    
