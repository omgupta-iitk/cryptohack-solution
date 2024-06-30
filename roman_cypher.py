s= input("ENTER THE CYPHER =>")


for i in range(1,27):
    ar = ""
    for st in s:
        if(st == ' '):
            ar+=' '
            continue
        ar =ar+ str(chr(65+(ord(st)-65+i)%26))
    print(ar)

# EBXOQ MRKZE MOFJXOV XAJFQ


