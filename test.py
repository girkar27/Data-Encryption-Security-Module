from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
from Crypto.Util.Padding import pad, unpad
from binascii import hexlify, unhexlify

 # key, iv, data, mode 
block_size  = AES.block_size 
iv = '4782583707RRHRBR'
key = '1496899267KMOWJE'
data = 'jai'
mode = 2

# def pad(text,pad_size=16):
#     text_length = len(text)
#     last_block_size = text_length % pad_size
#     remaining_space = pad_size - last_block_size
#     text = text + '='*remaining_space
#     return text



if mode==2:
    cipher = AES.new(key.encode('utf-8'), mode, iv.encode('utf-8'))
    ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), block_size))
    # encrypted_data = b64encode(ct_bytes).decode('utf-8')    
    cipher_text = hexlify(ct_bytes)
    rt = cipher_text.decode('utf-8')
    # print(rt)         

    hexToBinStr = unhexlify(rt)
    # rt = b64decode(hexToBinStr)
    cipher = AES.new(key.encode('utf-8'), mode, iv.encode('utf-8'))
    pt = unpad(cipher.decrypt(hexToBinStr), AES.block_size)
    print(pt.decode('utf-8'))
    
        


