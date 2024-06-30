from pwn import *
key = 0x73^ord("c")

print("".join(str(xor(b,key).decode()) for b in bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")))