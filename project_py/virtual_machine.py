
# Info:
# [0000]Operação;[0000]Endereço_Resultado;[0000]Endereço_1; [0000]Endereço_2
# Instruções:
# 0001: Soma
# 0010: Sub
# 0100: Load
# 1000: Store

# Constantes pré-definidas:
ZERO = 0b0000000000000000
FBITS = 0b0000000000001111

# Registradores:
PC = 0
Instr = ZERO
InstrType = ZERO
RegSourceA = ZERO
RegSourceB = ZERO
RegDest = ZERO
RegAddrMemory = ZERO
Reg = []
mem = []

D = 0
A = 0
B = 0


# Abrir arquivo de Memória para leitura
# file = open('progMemory.txt', 'r')
# Abrir arquivo de Programa para leitura
# file = open('code.txt', 'r')


def transform():
    InstrType = Instr >> 12
    InstrType = InstrType & FBITS
    print('InstrType ' + str(InstrType))
    RegDest = Instr >> 8
    RegDest = RegDest & FBITS
    print('RegDest ' + str(RegDest))
    RegSourceA = Instr >> 4
    RegSourceA = RegSourceA & FBITS
    print('RegSourceA ' + str(RegSourceA))
    RegSourceB = Instr
    RegSourceB = RegSourceB & FBITS
    print('RegSourceB ' + str(RegSourceB))
    decode()


# Inicialização de Funções
def decode():

    print('Decoding...')

    InstrType = Instr >> 12

    filem = open('progMemory.txt', 'r')

    # t = 0
    # for i in file:
    #     mem[t] = int(i, 2)
    #     t += 1

    if InstrType == 1:
        print('Somando...')
        # Resultado = mem[RegSourceA] + mem[RegSourceB]
        # Resultado = int(filem.readline(RegSourceA), 2) + int(filem.readline(RegSourceB), 2)
        # print('Resultado é ' + str(Resultado))
        # Soma

    elif InstrType == 2:
        print('Subtraindo...')
        # Sub

    elif InstrType == 4:
        print('Loading...')
        # Load:

    elif InstrType == 8:
        print('Storing...')
        # Store:

    filem.close()
    print('Decoded!')


def execute():
    print('Transforming...')
    transform()
    print('Results: \n')
    print('Command: ' + str(InstrType) + '\n')
    print('Final Addr: ' + str(RegDest) + '\n')
    print('A: ' + str(RegSourceA) + '\n')
    print('B: ' + str(RegSourceB) + '\n')


# Inicialização dos Registros
for i in range(11):
    Reg.append(0)

# Execução com for rodando todas as linhas do programa e executando direto
file = open('code.txt')

for i in file:
    Instr = int(i, 2)
    print(str(i))
    execute()

file.close()

# Execução do Programa
# while PC < 4:
#     file = open('code.txt', 'r')  # não precisa do r
#     Instr = int(file.readline(PC), 2)
#     file.close()
#     PC += 1
#     decode()
#     execute()
