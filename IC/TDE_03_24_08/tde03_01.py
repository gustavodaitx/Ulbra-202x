from pprint import pformat


pf=float(input("Digite o Preço de Fábrica:"))

imposto=((30*pf)/100)
revenda=((imposto*10)/100)
final=pf+imposto+revenda

print(f'O Preco final do Computador é:{final}')

