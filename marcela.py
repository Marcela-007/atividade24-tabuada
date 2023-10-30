# Exercício Python 24: Refaça a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.
tabuada = int(input('Digite um número: '))
 
for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )