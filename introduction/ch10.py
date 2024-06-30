byt =  bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

key = [byt[i]^ord(c) for i,c in enumerate("crypto{")]
key = key + [byt[-1]^ord('}')]
print("".join(chr(o) for o in key))
print("".join(chr(o^key[i%len(key)]) for i,o in enumerate(byt)))

