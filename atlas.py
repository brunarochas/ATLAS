#PROJETO ATLAS

p1 = input('Qual é o seu nome? ')
p2 = input('O que você quer estudar? ')
p3 = input('Qual é seu principal objetivo com esse estudo? ')
p4 = input('Qual conteúdo ou habilidade você precisa priorizar? ')
p5 = input('Como você avalia seu nível atual? (Iniciante, intermediário ou avançado.) ')
p6 = int(input('Quantas horas por semana você tem disponíveis? '))
p7 = int(input('Em quantos meses pretende atingir seu objetivo? '))


print('Olá {}! Você quer estudar {}.'.format(p1, p2)) 
print('Seu objetivo é {}. Você precisa priorizar {}.'.format(p3, p4))
print('Seu nível atual é {}. Você tem {} horas por semana e pretende atingir seu objetivo em {} meses.'.format(p5,p6,p7))