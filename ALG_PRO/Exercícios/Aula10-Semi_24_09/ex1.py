input("Qual seu nome completo: \n")
input("Qual seu rg: \n")
input("Qual seu cpf: \n")
input("Qual sua idade: \n")

saude=input(f" Você possui algum problema de saúde? sim ou não : \n")

print(15*"%===$===")

if saude=="sim":
    print("Você está dispensado do serviço militar em decorrência de problema de saúde !!\n ")
else:
    print("Candidato alistado corretamente !!")
    print("Parabéns")

