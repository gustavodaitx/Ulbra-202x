print("Seja bem vindo a academia Topmasters!!!\n ")
print("Trabalhamos com três tipos de planos !!!\n ")
print( " 2 vezes na semana, 3 vezes na semana e Livre")

print(15*"%===$===")

plano=float(input(f"\n Quantos dias na semana pretende frequentar a academia ( >=2 dias) ? : "))
print("Qual modalidade escolhida?")
modalidade=float(input(f"\n (1 )Musculacao, (2) musculacao + funcional (3) crossfit :"))

print(15*"%===$===")

musc_2x=80
musc_3x=100
musc_livre=120

musc_func_2x=120
musc_func_3x=140
musc_func_livre=170

cros_2x=120
cros_3x=160
cros_livre=200

if modalidade==1 and plano==2:
    print(f"\n Para fazer Musculação, 2 vezes na semana, você pagará R${musc_2x} mensais.")
if modalidade==1 and plano==3:
    print(f"\n Para fazer Musculação, 3 vezes na semana, você pagará R${musc_3x} mensais.")
if modalidade==1 and plano>3:
    print(f"\n Para fazer Musculação, mais de 3 vezes na semana, você pagará R${musc_livre} mensais.")

if modalidade==2 and plano==2:
    print(f"\n Para fazer Musculação + Funcional, 2 vezes na semana, você pagará R${musc_func_2x} mensais.")
if modalidade==2 and plano==3:
    print(f"\n Para fazer Musculação + Funcional, 3 vezes na semana, você pagará R${musc_func_3x} mensais.")
if modalidade==2 and plano>3:
    print(f"\n Para fazer Musculação + Funcional, mais de 3 vezes na semana, você pagará R${musc_func_livre} mensais.")
    
if modalidade==3 and plano==2:
    print(f"\n Para fazer Crossfit, 2 vezes na semana, você pagará R${cros_2x} mensais.")
if modalidade==3 and plano==3:
    print(f"\n Para fazer Crossfit, 3 vezes na semana, você pagará R${cros_3x} mensais.")
if modalidade==3 and plano>3:
    print(f"\n Para fazer Crossfit, mais de 3 vezes na semana, você pagará R${cros_livre} mensais.")

