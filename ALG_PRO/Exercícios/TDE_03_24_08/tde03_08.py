raio=float(input("Digite o raio do tanque (r): "))
altura=int(input("Digite a altura do tanque (a):  "))

custo_lata=150
litro_lata=5
cobertura=3
pi=3.14159
cobertura_por_lata=litro_lata*cobertura

area_base=pi*raio**2
area_lateral=2*pi*raio*altura
area_tanque=area_base+area_lateral


total_latas=(area_tanque/cobertura_por_lata)
total_custo=total_latas*custo_lata

print(f'Para pintar um tanque de cumbustível de raio= {raio}; e altura {altura}; com area total= {area_tanque:.2f}  m3; você gastará {total_latas} latas de tintas;e o custo será de R$ {total_custo:.2f}')
