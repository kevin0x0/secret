import crypt
import sys

filename = sys.argv[1]
key = crypt.buildkey(sys.argv[2])

with open(filename, "r") as f:
    content = f.read()

ciphertext = crypt.encrypt(content, key)
with open(filename + ".cipher", "w") as f:
    f.write(ciphertext)
