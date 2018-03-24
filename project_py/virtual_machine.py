
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

D = 0
A = 0
B = 0


# Abrir arquivo de Memória para leitura
# file = open('progMemory.txt', 'r')
# Abrir arquivo de Programa para leitura
# file = open('code.txt', 'r')


def transform():
    RegDest = Instr >> 8
    RegDest = Instr & FBITS
    RegSourceA = Instr >> 4
    RegSourceA = Instr & FBITS
    RegSourceB = Instr
    RegSourceB = Instr & FBITS


# Inicialização de Funções
def decode():

    print('Decoding...')

    InstrType = Instr >> 12

    file = open('progMemory.txt', 'r')

    if InstrType == 1:
        # Soma
        transform()
        # ler memória em binário

    elif InstrType == 2:
        # Sub
        transform()
        # ler memória em binário

    elif InstrType == 4:
        # Load:
        transform()

    elif InstrType == 4:
        # Load:
        transform()

    file.close()
    print('Decoded!')


def execute():
    print('Executing...')
    print('Executed...')


# Inicialização dos Registros
for i in range(11):
    Reg.append(0)

# Execução do Programa
while PC < 4:
    file = open('code.txt', 'r')
    Instr = file.readline(PC)
    file.close()
    PC += 1
    decode()
    execute()
