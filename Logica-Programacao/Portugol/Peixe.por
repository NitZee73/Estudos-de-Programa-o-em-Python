programa
{
	
	funcao inicio()
	{
	real quilosdepeixe
	real multa = 4.00
	real excesso
	real valor_a_pagar
	
		escreva("Insira a quantidade de peixe em Kg: ")
		leia (quilosdepeixe)
		
		se (quilosdepeixe > 50)
		{
		valor_a_pagar = (quilosdepeixe - 50) * multa
		escreva("valor da multa: $" , valor_a_pagar)
		}
		senao
		{
		escreva ("Quilos de peixe dentro do valor regulamentado, multa não será aplicada")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 312; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */