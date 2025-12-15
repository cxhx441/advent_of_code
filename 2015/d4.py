import hashlib

input_str = "ckczppom"

i = 0
zeropad = 5
while True:
    output = hashlib.md5((input_str + str(i)).encode())
    if output.hexdigest()[:zeropad] == '0'*zeropad:
        print(f'result: {output.hexdigest()}')
        print(i)
        break
    i += 1

i = 0
zeropad = 6
while True:
    output = hashlib.md5((input_str + str(i)).encode())
    if output.hexdigest()[:zeropad] == '0'*zeropad:
        print(f'result: {output.hexdigest()}')
        print(i)
        break
    i += 1
