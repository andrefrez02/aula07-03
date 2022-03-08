print('\n' * 20)
nome = input(f'Digite o do Aluno: ')
curso = input(f'Digite o nome do curso: ')
nota1 = input(f'Digite o valor da primeira nota do Aluno: ')
nota2 = input(f'Digite o valor da segunda nota do Aluno: ')

nota1 = float(nota1)
nota2 = float(nota2)

media = (nota1 + nota2) / 2

print(f'\nA primeira nota de {nome} é de: {nota1}\nA segunda nota de {nome} é de: {nota2}\nA média de {nome} é de: {media}')
print('\n' * 20)

if media >= 7:
    print(f'\n{nome} passou em {curso} com uma média de: {media} PARABÉNS!!!')
elif media >= 5 and media < 7:
    print(f'\n{nome} ficou de recuperação em {curso} com uma média de: {media} FAÇA O EXAME FINAL!!!')
else:
    print(f'\n{nome} não passou em {curso} com uma média de: {media} ESTUDE MAIS!!!')