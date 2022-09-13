tempo_gasto=float(input(" Digite o tempo de viagem em horas:  "))
velocidade_media=float(input("Digite a velocidade média em km/h:  "))

distancia=tempo_gasto*velocidade_media

litros_gastos=distancia/12


print(f'Você percorreu {distancia} Km, e gastou {litros_gastos} Litros de Gasolina')


