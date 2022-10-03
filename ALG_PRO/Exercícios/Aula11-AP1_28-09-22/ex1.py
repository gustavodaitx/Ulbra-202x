#aliquota_pis = 0.56% = 0.0065
#aliquota_cofins = 3% = 0.03

print("Vamos ver qual foi seu lucro este mês !!!")

Faturamento = float(input("\n Digite o Faturamento da Empresa no mês R$: ")) 
Custo = float(input("\n Digite o Custo de Produção mensal: "))

pis = Faturamento * 0.0065

cofins = Faturamento * 0.03

impostos = pis + cofins

lucro = Faturamento - impostos - Custo

print(15*"%===$===")

print(f"\n O faturamento da empresa neste mês foi de R$ {Faturamento}.\n")

print(15*"%===$===")

print( f"\n Você pagará R$ {pis} referente ao PIS.\n")

print(F"\n Você pagará R$ {cofins} referente ao COFINS\n")

print(15*"%===$===")

print(f"\n O Lucro da empresa foi de R$ {lucro} este mês.\n")

print("Parabéns")
print("      '._==_==_=_.'     ")
print("      .-\\:      /-.    ")
print("     | (|:.     |) |    ")
print("      '-|:.     |-'     ")
print("        \\::.    /      ")
print("         '::. .'        ")
print("           ) (          ")
print("         _.' '._        ")
print("        '-------'       ")



