preco_racao=float(input("Digite o preço da Ração:" ))

kg_saco=float(input(" DiGite quantos quilos tem o saco de ração:" ))

dias= float( input( "Digite a quantidade de dias que irá alimentar: "))

refeicao= float(input("Digite quantas refeicoes o cao fará:" ))

quantidade_racao=(dias*refeicao)*0.180

preco_kg=preco_racao/kg_saco

gasto_din= quantidade_racao*preco_kg

print(f'O custo para alimentar seu cao durante {dias}, é de R$ {gasto_din:.2f}')

