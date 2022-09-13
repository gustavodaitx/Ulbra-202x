n=float(input("Digite seu códido de funcionário: "))
h=float(input("Horas trabalhadas no mês: "))
vh=float(input("Valor por hora de trabalho: "))
f=float(input("filhos menores de 14 anos: "))
i=float(input("Qual sua idade: "))
ts=float(input("Tempo de serviço: "))

valor_horas_trabalhadas=h*vh

if valor_horas_trabalhadas<=1655.98:
    sf=f*56.47
    print(f'\nVocê terá direiro a R$ {sf} a título de Salário Família.\n')

else:
    sf=0
    
sb=h*vh+sf
inss= sb*0.085

if  sb>1500:
    ir=0.15*sb
    print(f'\nVocê pagará R${ir:.2f} de Imposto de Renda.\n')
    
elif    sb>500 and sb<1500:
        ir=0.08*sb
        print(f'\nVocê pagará R${ir:.2f} de Imposto de Renda.\n')

if  sb<500:
    ir=0
    print(f'\nVocê não terá incidência de IR.\n')
    
desc=inss+ir

sl=sb-desc

print(f'\nVocê terá desconto de R$ {inss:.2f} de INSS.\n')

print(f'\nFunc.Cód:{n}>Salário Bruto R${sb:.2f} - Descontos R${desc:.2f} = Salário LíquidoR$ {sl:.2f}.\n')

    

    


