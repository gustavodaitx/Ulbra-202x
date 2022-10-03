parede_altura=float(input("\n Qual a altura da parede ? (m): "))
parede_largura=float(input("\n Qual a largura da parede ? (m):"))

tijolo=float(input("\n Qual tipo de tijolo usado? 9 furos ou 12 furos ?: "))

# Tijolo 9 furos = 0.24cm larg x 0.14 cm alt = 0.0336 m 2 area#

# Tijolo 12 furos = 19cm larg x 19 cm alt = 0.0361 m 2 area #

area_total=parede_altura*parede_largura

print(15*"&==&==")

if tijolo==9:
    quant_tijolos=area_total / 0.0336
    print(f"\n Para fazer uma parede de {area_total:.0f}m2, com tijolos de 9 furos, serão necessários {quant_tijolos:.1f} tijolos.\n ")
else:
    quant_tijolos=area_total / 0.0361
    print(f"\n Para fazer uma parede de {area_total:.0f}m2, com tijolos de 12 furos, serão necessários {quant_tijolos:.1f} tijolos.\n ")

print(15*"&==&==")