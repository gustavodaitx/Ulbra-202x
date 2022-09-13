nome=input("Nome do Funcionário: \n")
salario=float(input("Salário atual R$: \n"))

print("-="*30)

print(f'Funcionário {nome}.')
print(f'Salário atual R$ {salario}')

print("-="*30)


if salario>0 and salario<=400.00:
    com_reajuste=(salario*0.15)+salario
    print("Seu aumento será de 15%")
    print("-="*30)
    print(f"Seu salário corrigido será de R$ {com_reajuste}")
    
elif salario>400.01 and salario<=700.00:
    com_reajuste=(salario*0.12)+salario
    print("Seu aumento será de 12%")
    print("-="*30)
    print(f"Seu salário corrigido será de R$ {com_reajuste}")

elif salario>700.01 and salario<=1000.00:
    com_reajuste=(salario*0.10)+salario
    print("Seu aumento será de 10%")
    print("-="*30)
    print(f"Seu salário corrigido será de R$ {com_reajuste}")

elif salario>1000.01 and salario<=1800.00:
    com_reajuste=(salario*0.07)+salario
    print("Seu aumento será de 7%")
    print("-="*30)
    print(f"Seu salário corrigido será de R$ {com_reajuste}")

elif salario>1800.01 and salario<=2500.00:
    com_reajuste=(salario*0.04)+salario
    print("Seu aumento será de 4%")
    print("-="*30)
    print(f"Seu salário corrigido será de R$ {com_reajuste}")

else:
    salario>=2500.01
    print("Você não terá reajuste !!")

