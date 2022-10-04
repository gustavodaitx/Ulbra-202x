preco_fabrica=float(input("digite o Preço de Fábrica: "))

imposto=(preco_fabrica*45)/100
margem=(preco_fabrica*28)/100

final=preco_fabrica+imposto+margem

print(f'O Valor final do Computador é de R$ {final:.2f}')