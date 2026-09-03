programa
{
	
	funcao inicio()
	{
	real salario, vendasV, Ncarros, salarioF
	real comissao = 0.05
	real comissaoFx = 500
	real comissaofinal
		escreva("Insira o salário base: $")
		leia(salario)
		escreva("Digite o valor total das vendas: $")
		leia(vendasV)
		escreva("Digite a quantidade de carros vendidos: ")
		leia(Ncarros)
		comissaofinal = ((comissaoFx * Ncarros) + (comissao * vendasV))
		salarioF = (comissaofinal + salario)
		escreva("O salário final é de: $" , salarioF)
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 124; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */