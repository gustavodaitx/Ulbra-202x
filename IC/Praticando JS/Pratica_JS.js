console.log("1 - Declarar uma variável, atribuir um valor numérico a ela..")
console.log("Mostrar o valor e o tipo. Teste todos os tipos vistos em sala de aula.")

//Declarar uma variável, atribuir um valor numérico a ela. 
//Mostrar o valor e o tipo. Teste todos os tipos vistos em sala de aula.
var numero = 13;
console.log("O número escolhido da Variável é  "  + numero)
console.log(typeof(numero));
var nomeDaPessoa = "Gustavo Daitx";
console.log("O nome da pessoa  é  "  + nomeDaPessoa)
console.log(typeof(nomeDaPessoa));
console.log(typeof(false));
console.log(typeof(null));

console.log("4 - Imprima a média aritmética de 3 números.")
//Imprima a média aritmética de 3 números.
var numero1 = 7;
console.log("O primeiro número  é "  +numero1)
var numero2 = 8;
console.log("O segundo número  é é "  +numero2)
var numero3 = 9;
console.log("O terceiro número é "  +numero3)
var saida = "imprime o resultado"

saida = (numero1+numero2+numero3)/3
console.log("A média é "  +saida)

console.log("5 - Simule as notas de um aluno da Ulbra. AP1, AP2, AS e média final.")

var notaAp1 = 8;
console.log("A sua primeira nota é "  +notaAp1)
var notaAp2 = 9;
console.log("A sua primeira nota é "  +notaAp2)
var notaAs = 7;
console.log("A sua primeira nota é "  +notaAs)

var saida = " imprime o resultado"
saida = (notaAp1+notaAp2+notaAs)/3
console.log(" A sua média final é" +  saida)

console.log("6 -Informe o nome e a idade de uma pessoa e imprima se esta pessoa é maior ou menor de idade.")

var nomeDaPessoa = "Gustavo Daitx";
var idadeDaPessoa = 41;
if (idadeDaPessoa=18){
    console.log(nomeDaPessoa,"você já é maior de idade!!");
}
else{
    console.log(nomeDaPessoa, " você ainda NÃO é maior de idade!!");
}

console.log("7 -Informe 3 números e mostre qual é o maior.")

var numero1 = 28;
console.log("O primeiro número  é "  +numero1)
var numero2 = 98;
console.log("O segundo número  é é "  +numero2)
var numero3 = 13;
console.log("O terceiro número é "  +numero3)

var maior = numero1;

if ( numero2>maior)
    maior = numero2;
if( numero3>maior)
    maior = numero3;
console.log("O maior número é " +  maior)








