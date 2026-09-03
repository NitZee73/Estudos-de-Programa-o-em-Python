programa
{
	
	funcao inicio()
	{
		inteiro numero, somapares = 0, somaimpares = 0
		
		
		escreva("Digite o número: ")
			leia(numero)
	enquanto (numero<=1000)
	{
		
		
		se (numero%2 ==0)
		
		{
			somapares = somapares + numero
		}
		
		
		senao
		{
		somaimpares = somaimpares + numero
		}
			
			
			
			
		escreva("Digite o número: ")
			leia(numero)
	}		
			
			
			escreva("\n Soma dos números pares: " , somapares)
			escreva("\n Soma dos números ímpares: " , somaimpares)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 488; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */