import sys
charset = '0123456789abcdefghijklmnopqrstuvxyzw '
def cript(Value):
    import time, hashlib, random
    Key = str(time.time()*100000).split(".")[0]
    Key2 = hashlib.md5(Key.encode('utf-8')).hexdigest()
    Key = str(hashlib.md5(str(hashlib.md5(Key.encode('utf-8')).hexdigest()).encode('utf-8')).hexdigest())+str(str(hashlib.md5(str(hashlib.md5(Key2.encode('utf-8')).hexdigest()).encode('utf-8')).hexdigest()))
    bValue = ""
    do = True
    aNum = [0,1,2,3,4,5,6,7,8,9]
    random.shuffle(aNum)
    for n in aNum:
        Key += str(n)
        if((n % 2) == 0 and do):
            Key += " "
            do = False
    bKey = ""
    for c in Key:
        if(bKey.find(c) == -1):
            bKey += c
    if(len(bKey) < len(charset)):
        ch = [c for c in charset]
        random.shuffle(ch)
        for c in ch:
            if(bKey.find(c) == -1):
                bKey += c
    for char in Value:
        bValue += bKey[charset.find(char)]

    return bValue, bKey


def decript(Value,Key):
    bValue = ""
    for char in Value:
        p = Key.find(char)
        p = charset[p]
        bValue += p
    return bValue


def Validador(v, k, c):
    if(decript(c,k) == v):
        return True
    else:
        return False









#Para usar com CMD
##print("")
##print("-"*10+"CRIPT"+"-"*10)
##if(len(sys.argv)==1):
##    print("Argumentos: \nA: Ajuda\nC: Criptografar\nD: Descriptografar")
##else:
##    if(sys.argv[1]=="A"):
##        print("Argumentos: \nA: Ajuda\nC: Criptografar\nD: Descriptografar")
##
##    if(sys.argv[1]=="C" or sys.argv[1]=="c"):
##        if(len(sys.argv)>2):
##            print("Criptografando...")
##            ret = cript(sys.argv[2])
##            print("String:",str(ret[0]),"\nKey:",str(ret[1]))
##        else:
##            print("Uso:\nCript.py C [VALOR]")
##    if(sys.argv[1]=="D" or sys.argv[1]=="d"):
##        if(len(sys.argv)>3):
##            print("Descriptografando...")
##            ret = decript(sys.argv[2],sys.argv[3])
##            print(str(ret))
##        else:
##            print("Uso:\nCript.py D [VALOR] [KEY]")


#Para rodar na IDLE
resp = input('C-> Criptografar\nD-> Descriptografar\nDigite:').lower()
if(resp == "c"):
    r = cript(input("String:").lower())
    print()
    print('String Criptografada:',r[0])
    print('Key para descriptografar:',r[1])
elif(resp == 'd'):
    print(decript(input('String:'),input('Key:')))
else:
    print("Opção inválida")
    



#Decript automático
#print("-DECRIPT-")
#
