from string import printable


a=int(input("Digite o número da sua conta: "))
b=float(input("Qual o saldo da sua conta: "))

if b>=0:
    print(f"Sua conta {a} está  NORMAL")
else:
    print(f"Conta número {a}")
    print("CONTA ESTOURADA")
    