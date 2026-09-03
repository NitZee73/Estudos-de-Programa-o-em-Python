programa
{
	
	funcao inicio()
	{
		real media
		inteiro numero, soma = 0, quantidade = 0
		
	escreva("Insira um número: ")
		leia (numero)



		enquanto (numero !=0){
			
			se(numero % 2 == 0 ) {
		
				soma = soma + numero
				quantidade++
				media = soma / quantidade
				
			}
			escreva("Insira um novo número: ")
				leia (numero)


			se(quantidade >0){
				
			}

		
		}

	escreva ("A soma dos números pares é: " , soma)
	escreva ("A média dos números pares é: " , media)
	escreva ("A quantidade de números pares somados é: " , quantidade)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 372; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */