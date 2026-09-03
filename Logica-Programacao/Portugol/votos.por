programa
{
	
	funcao inicio()
	{
	real votos, nulos, brancos, eleitores
real P_votos, P_nulos, P_brancos

escreva("Digite a quantidade de eleitores: ")
leia(eleitores)

escreva("Digite a quantidade de votos válidos: ")
leia(votos)

escreva("Digite a quantidade de votos nulos: ")
leia(nulos)

escreva("Digite a quantidade votos em branco: ")
leia(brancos)

P_votos = (votos / eleitores) * 100
P_nulos = (nulos / eleitores) * 100
P_brancos = (brancos / eleitores) * 100

escreva("O percentual de votos válidos é: ", P_votos, "%\n")
escreva("O percentual de votos nulos é: ", P_nulos, "%\n")
escreva("O percentual de votos em branco é: ", P_brancos, "%")
		
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 657; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */