a = 1
b = a + 2
print(a)
print(b)
print('something')
print('the answer is ' + str(b))

file = open('testfile.txt', 'w')

file.write('Hello World\n')
file.write('This is our new text file\n')
file.write('and this is another line.\n')
file.write('Why? Because we can.\n')

print('Ler todo o arquivo: \n')
file = open('testfile.txt', 'r')
print(file.read())

print('Somente um número determinado de caracteres(5): \n')
file = open('testfile.txt', 'r')  # arquivo precisa ser aberto antes de cada op
print(file.read(5))

print('Ler todas as linhas em vetor: \n')
file = open('testfile.txt', 'r')
print(file.readlines())

file.close()
