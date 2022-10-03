print(" Triagem Pré - Hemodiálise !!!")

peso_atual = float(input(" Qual seu peso atual ( Kg ) : "))

liquidos_ingeridos_24H = float(input("\nQuantos litros de líquidos você ingeriu hoje? : "))

peso_seco = peso_atual - liquidos_ingeridos_24H

print(15*"%===$===")

print(f" \n Seu peso seco é {peso_seco} Kg.")

print(15*"%===$===")

dif= peso_atual - peso_seco

print(f"\n A diferenca entre os dois é {dif:.2f} Kg.")

print(15*"%===$===")

if dif<1:
    print(f"\n Você não poderá realizar a heomiálise!!")

elif dif>=1 and dif< 2:
    print(f" \n Sua sessão de hemodiálise levará em torno de 2 Horas !")   

elif dif>=2 and dif< 3:
    print(f" \n Sua sessão de hemodiálise levará em torno de  3 Horas !")    

else:
    print(f"\nSua sessão de hemodiálise levará em torno de 4 Horas !")