programa
{
	
	funcao inicio()
	{
	inteiro n1, n2

		escreva("Insira o valor de n1: ")
		leia(n1)
		escreva("Insira o valor de n2: ")
		leia(n2)

		se(n1 > n2){
			escreva("O maior é: " , n1)
			escreva("\nA ordem crescene: " , n2, "," , n1)
		}
		senao{
			escreva("O maior é: " , n2)
			
			escreva("\nA ordem crescente é: " , n1,",", n2)
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 338; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */