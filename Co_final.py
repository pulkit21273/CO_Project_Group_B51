register = {
    "R0": "000",
    "R1": "001",
    "R2": "010",
    "R3": "011",
    "R4": "100",
    "R5": "101",
    "R6": "110",
    "V": "111",
    "L": "111",
    "G": "111",
    "E": "111",
}
registerDeclaration = {
    'R0': 0,
    'R1': 0,
    'R2': 0,
    'R3': 0,
    'R4': 0,
    'R5': 0,
    'R6': 0,
    "V": 0,
    "L": 0,
    "G": 0,
    "E": 0,
}
dict_repo = {
    "add": "10000",
    "sub": "10001",
    "mov": "10010",
    "ld": "10100",
    "st": "10101",
    "mul": "10110",
    "div": "10111",
    "rs": "11000",
    "ls": "11001",
    "xor": "11010",
    "or": "11011",
    "and": "11100",
    "not": "11101",
    "cmp": "11110",
    "jmp": "11111",
    "jlt": "01100",
    "jgt": "01101",
    "je": "01111",
    "hlt": "01010",
}
repo = {
    'typeA': {
        "add": "10000",
        "sub": "10001",
        "mul": "10110",
        "xor": "11010",
        "and": "11100",
        "or": "11011",
    },
    'typeB': {
        "mov": "10010",
        "ls": "11001",
        "rs": "11000",
    },
    'typeC': {
        "mov": "10011",
        "div": "10111",
        "not": "11101",
        "cmp": "11110",
    },
    'typeD': {
        "ld": "10100",
        "st": "10101",
    },
    'typeE': {
        "jmp": "11111",
        "jlt": "01100",
        "jgt": "01101",
        "je": "01111",
    },
    'typeF': {
        "hlt": "01010",
    }
}
variable = {}
variable_memory = {}


def checkLessThan(a, b):
    if a > b:
        return 0
    else:
        return 1


def checkEqual(a, b):
    if a == b:
        return 1
    else:
        return 0


def checkGreaterThan(a, b):
    if a > b:
        return 1
    else:
        return 0


'''def FlagGen(a, b):
    v = str(isOverflown(a, b))
    l = checkLessThan(a, b)
    g = checkGreaterThan(a, b)
    e = checkEqual(a, b)
    FLAG = "000000000000" + str(v) + str(l) + str(g) + str(e)
    return FLAG'''


def decimaltobinary(N):
    s = ""
    N = int(N)
    while N > 0:
        L = N % 2
        N = N//2
        s += str(L)
    s = s[::-1]
    return s.zfill(8)


# 220310151411
con = 0
errors = []


def error(i, statement):
    global errors
    errors.append("Error at line {}: Error: {} ".format(i, statement))


def pritErrors():
    for i in range(len(error)):
        print(errors[i])


'''def isOverflown(a, b, c, i):
    astr = str(bin(a))
    bstr = str(bin(b))
    cstr = str(bin(c))
    if(astr[0] == bstr[0] and cstr[0] != astr[0]):
        error(i+1, "Overflow")'''


def checkEightBit(a):
    if(a > 255):
        return False
    else:
        return True


labels = {}
isError = 0
Nerror = 0
x = 0
vari = 0


def storeFunctions():
    global isError
    global con
    global errors
    global x
    global vari
    if isError == 0:
        for i in range(0, len(inputList)):
            if(len(inputList[i]) == 0):
                continue
            else:
                if(inputList[i][0] == 'var'):
                    if con == 1:
                        error(i+1, "Varibles not delared earlier")
                        isError = 1
                        Nerror += 1
                    if len(inputList[i]) != 2:
                        error(i+1, "Invalid statement")
                        isError = 1
                        Nerror += 1
                    if(inputList[i][1] in variable.keys()):
                        error(i+1, "variable already declared")
                        isError = 1
                        Nerror += 1
                    else:
                        variable[str(inputList[i][1])] = 0
                        variable_memory[str(inputList[i][1])] = i+1
                        # print(variable_memory[str(inputList[i][1])])
                        vari += 1
                if(inputList[i][0] == 'ld'):
                    if(len(inputList[i]) != 3):
                        isError = 1
                        Nerror += 1
                        con = 1
                        error(i+1, "Invalid")
                    if(inputList[i][1] not in register.keys()):
                        error(i+1, "Invalid")
                        isError = 1
                        Nerror += 1
                        con = 1
                    else:
                        registerDeclaration[str(inputList[i][1])
                                            ] = variable[str(inputList[i][2])]

                if(inputList[i][0] == 'st'):
                    if(len(inputList[i]) != 3):
                        isError = 1
                        Nerror += 1
                        con = 1
                        error(i+1, "Invalid")
                    if(inputList[i][1] not in register.keys()):
                        error(i+1, "Invalid")
                        isError = 1
                        Nerror += 1
                        con = 1
                    else:
                        variable[str(inputList[i][2])
                                 ] = registerDeclaration[str(inputList[i][1])]


def errorHandling(inputList, i, n):
    global con
    global isError
    global Nerror
    if(inputList[i][0] not in dict_repo.keys() and inputList[i][0] != 'var'):
        error(i+1, "Invalid command")
        isError = 1
        Nerror += 1
    else:
        if(inputList[i][0] in repo['typeA'].keys()):
            u = 0
            if(len(inputList[i]) != 4):
                isError = 1
                con = 1
                u = 1
                Nerror += 1
                error(i+1, "Invalid syntax")
            if(u == 0 and (inputList[i][1] not in register.keys() or inputList[i][2] not in register.keys() or inputList[i][3] not in register.keys())):
                error(i+1, "Invalid registers")
                isError = 1
                Nerror += 1
                con = 1
            if(u == 0 and (inputList[i][1] == 'Flag' or inputList[i][2] == 'Flag' or inputList[i][3] == 'Flag')):
                error(i+1, "incoorect use of Flag")
                isError = 1
                Nerror += 1
                con = 1
            '''if(isOverflown(inputList[i][1], inputList[i][2], inputList[i][3], i)):
                error(i+1, "overflow detected")
                isError = 1
                Nerror += 1
                con = 1'''
        if(inputList[i][0] in repo['typeB'].keys()):
            u = 0
            o = str(inputList[i][2])

            if(str(o[1:]).isnumeric() == False):
                isError = 1
                Nerror += 1
                u = 1
                con = 1
                error(i+1, "exected a decimal number")
            if(inputList[i][1] not in register.keys()):
                isError = 1
                Nerror += 1
                u = 1
                con = 1
            if(inputList[i][1] == 'Flag' or inputList[i][2] == 'Flag'):
                if(inputList[i][0] != 'mov'):
                    error(i+1, "incoorect use of Flag")
                    isError = 1
                    Nerror += 1
                    con = 1
            if(o[0] != '$'):
                error(i+1, "No $ sign ")
                isError = 1
                Nerror += 1
                con = 1
                u = 1
                error(i+1, "Invalid register")
            if(checkEightBit(int(o[1:])) == False and u == 0):
                error(i+1, "Not an 8 bit number")
                isError = 1
                Nerror += 1
                con = 1

        if(inputList[i][0] in repo['typeC'].keys()):
            if inputList[i][0] == 'div':
                if registerDeclaration(str(inputList[i][1])) == 0:
                    error(i+1, "ZeroDivisionError")
                    con = 1
            if inputList[i][0] == 'mov':
                u = 0
                if(len(inputList[i]) != 3):
                    error(i+1, "Invalid syntax")
                    isError = 1
                    con = 1
                    Nerror += 1
                if(inputList[i][1] == 'Flag' or inputList[i][2] == 'Flag'):
                    error(i+1, "incoorect use of Flag")
                    isError = 1
                    Nerror += 1
                    con = 1
                if(inputList[i][1] not in register.keys()):
                    error(i+1, "Invalid Register")
                    isError = 1
                    con = 1
                    Nerror += 1
                if(o[0] != '$'):
                    error(i+1, "No $ sign ")
                    isError = 1
                    Nerror += 1
                    con = 1
                    u = 1
                    error(i+1, "Invalid register")
                if(u == 0 and checkEightBit(int(o[1:])) == False):
                    error(i+1, "Not an 8 bit number")
                    isError = 1
                    Nerror += 1
                    con = 1
            else:
                if(len(inputList[i]) != 3):
                    error(i+1, "Invalid syntax")
                    isError = 1
                    con = 1
                    Nerror += 1
                if(inputList[i][1] == 'Flag' or inputList[i][2] == 'Flag'):
                    error(i+1, "incoorect use of Flag")
                    isError = 1
                    Nerror += 1
                    con = 1
                if(inputList[i][1] not in register.keys()):
                    error(i+1, "Invalid Register")
                    isError = 1
                    con = 1
                    Nerror += 1
            '''if(isOverflown(inputList[i][1], inputList[i][2], i)):
                error(i+1, "overflow detected")
                isError = 1
                Nerror += 1
                con = 1'''
        if(inputList[i][0] in repo['typeD'].keys()):
            if(len(inputList[i]) != 3):
                isError = 1
                con = 1
                Nerror += 1
                error(i+1, "Invalid syntax")
            if(inputList[i][1] == 'Flag' or inputList[i][2] == 'Flag'):
                error(i+1, "incoorect use of Flag")
                isError = 1
                Nerror += 1
                con = 1

            '''if(checkMemory(inputList[i][2]) == False):
                isError = 1
                error(i+1, "Invalid")
                Nerror += 1'''
        if(inputList[i][0] in repo['typeE'].keys()):

            if(len(inputList[i]) != 2):
                isError = 1
                con = 1
                Nerror += 1
                error(i+1, "Invalid syntax")
            if(inputList[i][1] == 'Flag'):
                error(i+1, "incoorect use of Flag")
                isError = 1
                Nerror += 1
                con = 1
            '''if(checkMemory(inputList[i][2]) == False):
                isError = 1
                Nerror += 1
                error(i+1, "Invalid")'''
        if(inputList[i][0] in repo['typeF'].keys()):
            if(len(inputList[i]) != 1):
                isError = 1
                Nerror += 1
                con = 1
                error(i+1, "Invalid syntax")
            if(i != n-1):
                error(i+1, "hlt not as last")
                Nerror += 1
                isError = 1
                con = 1


n = int(input("Enter number of instructions: "))


def printBinary(l, n):
    global vari
    if (l[0] == "add"):
        registerDeclaration[l[3]] = registerDeclaration.get(
            l[2])+registerDeclaration.get(l[1])
    if (l[0] == "sub"):
        registerDeclaration[l[3]] = registerDeclaration.get(
            l[1])-registerDeclaration.get(l[2])
    if (l[0] == "mul"):
        registerDeclaration[l[3]] = registerDeclaration.get(
            l[1])*registerDeclaration.get(l[2])
    '''if (l[0] == "ld"):
        registerDeclaration[l[1]] = variables.get(l[2])
    if (l[0] == "st"):
        registerDeclaration[l[2]] = variables.get(l[1])'''
    if (l[0] == "xor"):
        registerDeclaration[l[3]] = registerDeclaration.get(
            l[1]) ^ registerDeclaration.get(l[2])
    if (l[0] == "or"):
        registerDeclaration[l[3]] = registerDeclaration.get(
            l[1]) | registerDeclaration.get(l[2])
    if (l[0] == "and"):
        registerDeclaration[l[3]] = registerDeclaration.get(
            l[1]) & registerDeclaration.get(l[2])
    if (l[0] == "not"):
        registerDeclaration[l[2]] = ~registerDeclaration.get(l[1])
    if (l[0] in repo['typeA'].keys()):
        print(dict_repo.get(l[0])+"00"+register.get(l[1]) +
              register.get(l[2])+register.get(l[3]))
    if (l[0] == "not" or l[0] == "cmp" or l[0] == "div"):
        print(dict_repo.get(l[0])+"00000" +
              register.get(l[1])+register.get(l[2]))
    if (l[0] == "ld" or l[0] == "st"):
        print(dict_repo.get(l[0])+register.get(l[1]) +
              decimaltobinary(n-vari+variable_memory[str(l[2])]-1))
    if (l[0] == "je" or l[0] == "jgt" or l[0] == "jlt" or l[0] == "jmp"):
        print(dict_repo.get(l[0])+"000"+variable.get(l[1]))
    if (l[0] == "rs" or l[0] == "ls"):
        print(dict_repo.get(l[0])+register.get(l[1])+decimaltobinary(l[2]))
    if (l[0] == "mov" and l[2] not in register):
        s = str(l[2])
        s = s[1:]
        print(dict_repo.get(l[0])+register.get(l[1]) + decimaltobinary(s))
    elif(l[0] == "mov" and l[2] in register):
        print(dict_repo.get(l[0])+"00000" +
              register.get(l[1])+register.get(l[2]))
    if (l[0] == "hlt"):
        print(dict_repo.get(l[0])+"00000000000")


t = n
inputList = []
totalCommmands = 0
while(n > 0):
    temp = [i for i in input().split()]
    if(':' in temp):
        inputList.append(temp[1:])
        y = temp[0].rstrip(':')
        labels[str(y)] = decimaltobinary(n-t)
    else:
        inputList.append(temp)

    totalCommmands += 1
    n = n-1

storeFunctions()
for i in range(totalCommmands):
    if(len(inputList[i]) == 0):
        continue
    errorHandling(inputList, i, totalCommmands)

if(inputList[n-1] != []):
    if inputList[n-1][0] != 'hlt':
        error(i+1, "no halt")
        isError = 1
else:
    if inputList[n-2][0] != 'hlt':
        error(i+1, "no halt")
        isError = 1

if(isError == 0):
    for i in inputList:
        if(i == []):
            continue
        printBinary(i, t)
else:
    for i in errors:
        print(i)
