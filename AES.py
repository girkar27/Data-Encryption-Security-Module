from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
from Crypto.Util.Padding import pad, unpad
from binascii import hexlify, unhexlify

class AES_en:
    # CFB = 3  #AES.MODE_CFB
    # CBC = 2  #AES.MODE_CBC
    # ECB = 1  #AES.MODE_ECB
    # OFB = 5  #AES.MODE_OFB
    def __init__(self, data=None, key=None, mode=None, iv=None):
        self.data = data
        self.key = key
        self.mode = mode
        self.iv = iv

    def validateParams(self):
        if self.data != None and self.key != None and self.mode != None:
            return True
        else:
            return False
    
    def encrypt(self): # key, iv, data, mode 
        block_size  = AES.block_size 
        iv = self.iv
        key = self.key
        data = self.data
        mode = self.mode

        if mode==3:
            cipher = AES.new(key.encode('utf-8'), mode, iv.encode('utf-8'))
            ct_bytes = cipher.encrypt(data.encode('utf-8'))
            if self.iv:
                iv = self.iv
            else:
                iv = b64encode(cipher.iv).decode('utf-8')
            encrypted_data = b64encode(ct_bytes).decode('utf-8')

        if mode==2:
            cipher = AES.new(key.encode('utf-8'), mode, iv.encode('utf-8'))
            ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), block_size))
            if self.iv:
                iv = self.iv
            else:
                iv = b64encode(cipher.iv).decode('utf-8')
            encrypted_data = b64encode(ct_bytes).decode('utf-8')

        if mode==1:
            cipher = AES.new(key.encode('utf-8'), mode)
            ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), block_size))
            encrypted_data = b64encode(ct_bytes).decode('utf-8')

        if mode==5:
            cipher = AES.new(key.encode('utf-8'), mode, iv.encode('utf-8'))
            ct_bytes = cipher.encrypt(data.encode('utf-8'))
            if self.iv:
                iv = self.iv
            else:
                iv = b64encode(cipher.iv).decode('utf-8')
            encrypted_data = b64encode(ct_bytes).decode('utf-8')
        return encrypted_data

    def decrypt(self):
        iv = self.iv
        mode = self.mode
        key = self.key
        rt = b64decode(self.data)

        if mode ==2:
            cipher = AES.new(key.encode('utf-8'), mode, iv.encode('utf-8'))
            pt = unpad(cipher.decrypt(rt), AES.block_size)
        
        if mode==3:
            cipher = AES.new(key.encode('utf-8'), mode, iv.encode('utf-8'))
            pt = cipher.decrypt(rt)
        
        if mode == 1:
            cipher = AES.new(key.encode('utf-8'), self.mode)
            pt = cipher.decrypt(rt)
        
        if mode == 5:
            cipher = AES.new(key.encode('utf-8'), self.mode, iv.encode('utf-8'))
            pt = cipher.decrypt(rt)
        return pt

    def encryptHex(self): # key, iv, data, mode 
        block_size  = AES.block_size 
        iv = self.iv
        key = self.key
        data = self.data
        mode = self.mode

        if mode==3:
            cipher = AES.new(key.encode('utf-8'), mode, iv.encode('utf-8'))
            ct_bytes = cipher.encrypt(data.encode('utf-8'))

        if mode==2:
            cipher = AES.new(key.encode('utf-8'), mode, iv.encode('utf-8'))
            ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), block_size))    

        if mode==1:
            cipher = AES.new(key.encode('utf-8'), mode)
            ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), block_size))    
            

        if mode==5:
            cipher = AES.new(key.encode('utf-8'), mode, iv.encode('utf-8'))
            ct_bytes = cipher.encrypt(data.encode('utf-8'))

        cipher_text = hexlify(ct_bytes)
        rt = cipher_text.decode('utf-8')
        return rt
            

    def decryptHex(self):
        iv = self.iv
        mode = self.mode
        key = self.key
        rt = unhexlify(self.data)

        if mode ==2:
            cipher = AES.new(key.encode('utf-8'), mode, iv.encode('utf-8'))
            pt = unpad(cipher.decrypt(rt), AES.block_size)
        
        if mode==3:
            cipher = AES.new(key.encode('utf-8'), mode, iv.encode('utf-8'))
            pt = cipher.decrypt(rt)
        
        if mode == 1:
            cipher = AES.new(key.encode('utf-8'), self.mode)
            pt = cipher.decrypt(rt)
        
        if mode == 5:
            cipher = AES.new(key.encode('utf-8'), self.mode, iv.encode('utf-8'))
            pt = cipher.decrypt(rt)
        
        decrypted = pt.decode('utf-8')        
        return decrypted

    def require_pkcs5(self):
        self.pad_method = 'pkcs5'
        


