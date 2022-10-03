print(" \n Seja bem vindo !!!\n ")

tempo_fumante = float(input("\nA quanto tempo você fuma (meses)?: "))
cigarro = float(input("\nQuantos cigarros você consumiu hoje?: "))

# 1 dia tem 1440 min #
# 1 cigarro perde 15 min #

dia_min=1440

dias = 30*tempo_fumante

perda_vida = cigarro * (15)

vida_perdida = perda_vida * dias 

dias_perdidos = vida_perdida / dia_min

print(15*"%===$===")

print(f"\nVocê perdeu {vida_perdida} minutos de vida!!\n")

print(f" \n Isso dá aproximadamente {dias_perdidos:.0f} dias a menos !\n")

print(15*"%===$===")


if dias<=90:
    print("\n Seus dentes devem estar amarelos nessa fase!")
    
elif dias<90 and dias>365:
    print("\n Você deve estar com Perda de Paladar e Respiração Comprometida, nesta faze.")
    
else:
    print("\n Infelizmente seu pulmão já está comprometido \n ")
    
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")