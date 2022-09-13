capital=float(input("Digite o valor do Emprestimo: "))
prazo=float(input("Digite o prazo do emprestimo em meses: "))
tx=float(input("Digite a taxa de juros mensal: "))

preco_racao_ano_c_=2628

taxa=tx/100

juros=capital*taxa*prazo

print(f'Você pagará R${juros} de juros,por R$ {capital} emprestado por {prazo} meses a taxa mensal de juros de {tx} %am')
