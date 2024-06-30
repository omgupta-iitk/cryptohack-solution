from pwn import *
KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
# print(int(bytes.fromhex('62').decode()) ^ int(bytes.fromhex('63').decode()))

a1 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
key1 = bytes.fromhex(KEY1)
a2 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")

temp = xor(xor(a1,key1),a2)
print(temp)

