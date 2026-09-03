def calc_inss(salario_bruto):
    if salario_bruto <= 2000.00:
        inss = salario_bruto * 0.07
    else:
        inss = salario_bruto * 0.09
    salario_final = salario_bruto - inss
    return salario_final


salario_bruto = float(input('Digite o salário bruto do funcionário: R$ '))
salario_final = calc_inss(salario_bruto)
print(f'O salário final do funcionário é: R$ {salario_final:.2f}')
