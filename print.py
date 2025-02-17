print('Imprime a mensagem e muda de linha')
print("Imprime a mensagem e permanece na linha", end='')#nao é para ter quebra de linha para o proximo print
print(" Continuo na mesma linha")

nome="Maria"
idade = 30
peso = 100

msg_formatada = 'O nome dela é {0} e ela tem {1} anos.'.format(nome, idade)
print(msg_formatada)

msg = f'Ola, meu nome é {nome} e eu peso {peso} quilos'

print(msg)