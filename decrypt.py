import crypt
import sys

filename = sys.argv[1]
key = crypt.buildkey(sys.argv[2])

with open(filename + ".cipher", "r") as f:
    ciphertext = f.read()

plaintext = crypt.decrypt(ciphertext, key)
with open(filename, "w") as f:
    f.write(plaintext)
