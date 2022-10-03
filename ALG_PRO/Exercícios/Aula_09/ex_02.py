faturamento = float(input('Qual o seu faturamento mensal? '))
 
pis = faturamento * 0.0065
cofins = faturamento * 0.03
 
print(f'Com base no faturamento de {faturamento} sua empresa pagará de PIS R${pis} e de COFINS R$ {cofins}.')
