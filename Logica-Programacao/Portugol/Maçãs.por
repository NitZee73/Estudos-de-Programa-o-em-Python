programa
{
	
	funcao inicio()
	{
	real fruta, fruta11 = 1.30, fruta12 = 1.00, Vfinal
		escreva("Qual a quantidade de maçãs?: ")
		leia(fruta)

		se (fruta<12){
		Vfinal = fruta11 * fruta
		escreva("\nO valor das frutas é: $" , Vfinal)
		}

		senao { 
		Vfinal = (fruta12 * fruta)
		escreva("\nO valor das frutas é: $" , Vfinal)
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 337; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */