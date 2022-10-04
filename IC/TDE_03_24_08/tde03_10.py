vendedor=input("Nome do vendedor:")
codigo=float(input("Código do Vendedor: "))    
vendas=float(input(f'Número Carros Vendidos no mês por {vendedor}: '))
tvendas= float(input(f'Qual a soma em valores dos carros vendiso por {vendedor}: '))

fixo=980.00

comissao=(tvendas*2)/100

salario=fixo+comissao

print(f' Vendedor Código {codigo} : {vendedor}, receberá este mês o salário de R$ {salario:.2f}')





