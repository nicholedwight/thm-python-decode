import base64

file = open("encodedflag.txt", "r")

read = file.readline()

encrypted = ""

for i in range(0,5):
    encrypted = base64.b16decode(read)
    read = encrypted

for i in range(0,5):
    encrypted = base64.b32decode(read)
    read = encrypted

for i in range(0,5):
    encrypted = base64.b64decode(read)
    read = encrypted

print(read)

file.close()