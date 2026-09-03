programa
{
	
	funcao inicio()
	{
	real Cfabrica, Pdistribuidor = 0.28, impostos = 0.45, Vfinal, Pfinal, Pfinal_imposto, Pfinal_distribuidor
		escreva("Qual o valor de fabicação: $")
		leia(Cfabrica)
		Pfinal_imposto = (Cfabrica * impostos)
		Pfinal_distribuidor = (Cfabrica * Pdistribuidor)
		Vfinal = (Pfinal_imposto + Pfinal_distribuidor + Cfabrica)
		escreva("O valor final do carro é: $" , Vfinal)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 0; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */