# > CONDICIONAIS

idade = 20

if idade >= 18:
    print('Voçê é maior de idade.')
else:
    print('Voçê é menor de idade.')
    
# ':' serve como um então e deve ser usado para seguir com o comando de função    
"""
    imagine que voçê queira imprimir "Aprovado(a)", caso o estudante tenha uma média
    superior ou igual a 7, e "Reprovado", caso a média seja inferior a 7 
"""

media = float(input('Informe a média do estudante: '));

if media >= 7:
    print('Voçê foi Aprovado(a)!')
elif media >= 5:
    print('Recuperação.')
else:
    print('Voçê foi Reprovado(a).')
    
    
    media = 10
    presenca = 100
    
if media >= 7 and presenca >= 70:
    print('Aprovado!')
else:
    print('Reprovado')