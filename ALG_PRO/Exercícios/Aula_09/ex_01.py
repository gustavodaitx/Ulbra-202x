capital=float(input("Qual valor Empréstimo: "))
prazo=float(input("Qual o prazo do empréstimo: "))



if prazo<=10:
    
    montante=capital* ((1+ 0.016)**prazo)
    
    print(f'Você pagará R$ {montante:.2f} pelo empréstimo de R$ {capital} em {prazo} vezes')

elif prazo>10 and prazo<=24:
    
    montante=capital* ((1+ 0.018)**prazo)
    
    print(f'Você pagará R$ {montante:.2f} pelo empréstimo de R$ {capital} em {prazo} vezes')

else:
    
    montante=capital* ((1+ 0.02)**prazo)
    
    print(f'Você pagará R$ {montante:.2f} pelo empréstimo de R$ {capital} em {prazo} vezes')