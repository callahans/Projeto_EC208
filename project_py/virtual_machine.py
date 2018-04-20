
# Info:
# [0000]Operação;[0000]Endereço_Resultado;[0000]Endereço_1; [0000]Endereço_2
# Instruções:
# 0001: Soma
# 0010: Sub
# 0100: Load
# 1000: Store


# Registradores:


InstrType = ''

# Abrir arquivo de Memória para leitura
# file = open('progMemory.txt', 'r')
# Abrir arquivo de Programa para leitura
# file = open('code.txt', 'r')





def decode(Instr):


    InstrType = Instr[:4]

    try:
        InstrType = int(InstrType,2)
    except:
        print(InstrType)
        print(type(InstrType))

    if InstrType == 1 :
        # Add

        print('SOMANDO...\n')

        A = int(Instr[8:12],2)
        B = int(Instr[12:16],2)

        C = A + B
        C = bin(C)
        C = C[:1] + C[2:5]

        Instr = Instr[:4] + C + Instr[8:16]

        print('RegSourceA: {}'.format(Instr[8:12]))
        print('RegSourceB: {}'.format(Instr[12:16]))
        print('Result: {}'.format(C))

        fileMem = open('progMemory.txt', 'a')
        fileMem.write('{} {} {} {}'.format(Instr[:4],Instr[4:8],Instr[8:12],Instr[12:16]) + '\n')
        fileMem.close()




    elif InstrType == 2:
        # Sub
        print('SUBTRAINDO...\n')

        A = int(Instr[8:12],2)
        B = int(Instr[12:16],2)

        C = A - B

        if C == 3 or C == 2:
            C = '0' + bin(C)
            C = C[:2] + C[3:5]

        elif C == 0 or C == 1:
                C = '00' + bin(C)
                C = C[:3] + C[4:5]
        else:
            C = C[:1] + C[2:5]




        Instr = Instr[:4] + C + Instr[8:16]


        print('RegSourceA: {}'.format(Instr[8:12]))
        print('RegSourceB: {}'.format(Instr[12:16]))
        print('Result: {}'.format(C))

        fileMem = open('progMemory.txt', 'a')
        fileMem.write('{} {} {} {}'.format(Instr[:4],Instr[4:8],Instr[8:12],Instr[12:16]) + '\n')
        fileMem.close()



    elif InstrType == 4:
        # Load:
        print('LOADING...\n')
        print('RegDest: {}'.format(Instr[4:8]))
        print('RegSourceA: {}'.format(Instr[8:12]))
        print('RegSourceB: {}'.format(Instr[12:16]))


    elif InstrType == 8:
        # Store:
        print('STORING...\n')
        print('RegDest: {}'.format(Instr[4:8]))
        print('RegSourceA: {}'.format(Instr[8:12]))
        print('RegSourceB: {}'.format(Instr[12:16]))


    print('\n\nDecoded!')





def execute(Instr):


    print('\n\nCommand: {}'.format(Instr[:4]),'\n')

    decode(Instr)
    print('-------------------------------------')




# Execução com for rodando todas as linhas do programa e executando direto
file = open('code.txt', 'r')

for line in file:

    line = line.rstrip()
    Instr = line

    try:
        execute(Instr)
    except:
        print(Instr)
        print(type(Instr))
file.close()
