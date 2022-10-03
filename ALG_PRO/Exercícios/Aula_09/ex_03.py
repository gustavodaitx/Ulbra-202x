tempo = float(input('Qual o tempo que o corredor levou para percorrer 10km? '))
 
if tempo <= 35:
    print(f'O Corredor marcou 10 pontos ao correr 10km em {tempo} minutos.')
elif tempo > 35 and tempo <= 40:
    print(f'O Corredor marcou 8 pontos ao correr 10km em {tempo} minutos.')
else:
    print(f'O Corredor marcou 5 pontos ao correr 10km em {tempo} minutos.')
