dias=int(input("Digite o número de diárias: "))

valor_diaria=50.00*dias

if dias<15:
    servico=1.5*dias

if dias==15:
    servico=1*dias

else:
    
    servico=0.50*dias

a_pagar=valor_diaria+servico

print("-="*30)

print(f'Você pagará R$ {a_pagar:.2f}, pelos seus {dias} de lazer !!')
