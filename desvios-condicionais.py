n1 = n2 = 0.0
media = 0.0

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media  = (n1 + n2) / 2

if (media >= 7):
  print("Aprovado com a media", media)
elif (media >= 5):
  print("Voce esta de recuperacao com a media", media)
else:
  print("Aluno reprovado com a media", media)
  