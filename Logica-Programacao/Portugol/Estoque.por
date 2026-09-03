programa
{
	
	funcao inicio()
	{
	inteiro quantidade_em_estoque
	inteiro quantidade_maxima_estoque = 580
	inteiro quantidade_minima_estoque = 270
	inteiro quantidade_media

	
		escreva("Insira a quantidade em estoque: ")
		leia (quantidade_em_estoque)
		quantidade_media = (quantidade_maxima_estoque + quantidade_minima_estoque) / 2
		
		se (quantidade_em_estoque >= quantidade_media)
		{
			escreva ("Não efetuar compra")
		}
		senao
		{
			escreva("Efetuar compra")
		}

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 389; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */