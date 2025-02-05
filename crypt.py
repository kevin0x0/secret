from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt(plain_text: str, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv + ':' + ct

def decrypt(ciphertext: str, key):
    iv, ct = ciphertext.split(':')
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
    return pt

def buildkey(originkey: str):
    return bytes(originkey[0:16] if len(originkey) > 16 else
                 originkey.zfill(16), encoding='utf-8')
