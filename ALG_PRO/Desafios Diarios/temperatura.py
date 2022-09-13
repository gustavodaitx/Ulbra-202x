celcius=float(input("Digite a Temperatura em Celcius: "))

fahrenheit=1.8*(celcius)+32

kelvin=celcius+273

fa_para_Ke=5/9*(fahrenheit-32)+273,15

print(f'A temperatura {celcius} ºC, é a mesma que {fahrenheit}ºF, e {kelvin} ºK')
