programa
{
	
	funcao inicio()
	{
	real salario, reajuste, novosalario
		escreva("Digite o valor do salário atual: $")
		leia(salario)
		escreva("Digite o valor do reajuste: " ,"%")
		leia(reajuste)
		novosalario = (((reajuste /100) * salario) + salario)
		escreva("O novo salário é: $" , novosalario)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 294; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */