programa
{
	
	funcao inicio()
	{
	 real jornada = 160.0, jornadatotal, acrecimo = 1.5, salario, novosalario, horaextra,salarioporhora
		escreva("Qual foi a Jornada de trabalho do funcionário neste mês?: ")
		leia(jornadatotal)
		escreva("Qual o salário so funcionário:? $")
		leia(salario)
		horaextra=(jornadatotal-jornada)
		salarioporhora=(salario/jornada)

	se(jornadatotal > jornada){
		novosalario=(salario + (salarioporhora * horaextra * acrecimo))
		escreva("O novo salário é: $" , novosalario)
		

		
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 525; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */