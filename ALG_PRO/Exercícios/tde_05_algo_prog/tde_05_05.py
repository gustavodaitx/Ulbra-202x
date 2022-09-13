codigo=int(input("Digite o código do Aluno:  "))
n1=float(input("Digite a nota 01 ( 0 a 10):  "))
n2=float(input("Digite a nota 02 ( 0 a 10):  "))
n3=float(input("Digite a nota 03 ( 0 a 10):  "))

nota_maior=max(n1,n2,n3)


peso4=nota_maior*4


duas_notas=(n1+n2+n3)-nota_maior

peso3=duas_notas*3


mp=(peso4+peso3)/(4+3+3)


if mp>=7:
    print("-="*30)
    print(f'Aluno cód:{codigo}, \nObteve notas: {n1},{n2} e {n3}.\nSua média é {mp:.2f}.\n !!! APROVADO !!!\n')
else: 
    mp<7
    print("-="*30)
    print(f'Aluno cód:{codigo}, \nObteve notas: {n1},{n2} e {n3}.\nSua média é {mp:.2f}.\n !!! REPROVADO !!!\n')
    

