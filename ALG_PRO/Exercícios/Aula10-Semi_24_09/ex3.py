betoneira = int(input("Qual a quantidade de betoneira que você deseja fazer?: "))

massa = input("Qual o tipo de massa?:")

areia = 0

cimento = 0

brita = 0

if massa == "concreto":
    ciemento = betoneira * 5
    areia = cimento * 3
    brita = cimento * 3
    
    print( f"Com{betoneira} betoneiras, você gastará de material:cimento:{cimento} baldes, areia:{areia} baldes e brita:{brita} baldes")

else:
    cimento = betoneira * 5 
    
    areia =  cimento * 5 
    
    brita = 0 

    print( f"Com{betoneira} betoneiras, você gastará de material:cimento:{cimento} baldes, areia:{areia} baldes e brita:{brita} baldes")
