from RequestValidate import RequestValidate
from AES import AES_en
from hashlib import sha1

class TransactionResponseBean(RequestValidate):

    responsePayload = ""

    key= None

    iv= None
    
    mode = 2

    def set(self, field, value):
        self.field = value

    def getMode(self):
        return self.mode

    def setResponsePayload(self, responsePayload):
        self.responsePayload =  responsePayload
        return self.responsePayload

    def setMode(self, mode):
        self.mode = mode
        return self.mode 

    def setKey(self, key):
        self.key = key
        return self.key
    
    def setIv(self, iv):
        self.iv = iv
        return self.iv

    def getResponsePayload(self):
        responseParams = {
            'pRes': self.responsePayload,
            'pEncKey': self.key,
            'pEncIv': self.iv
        }

        errorResponse = self.validateResponseParam(responseParams = responseParams)

        if errorResponse:
            return errorResponse
        
        aesObj = AES_en(self.responsePayload, self.key, self.mode, self.iv)
        aesObj.require_pkcs5()
        response =  aesObj.decrypt()
        decryptResponse = response.decode('utf-8') 
        implodedResp = decryptResponse.split('|')
        hashCodeString = implodedResp.pop()
        explodedHashValue = hashCodeString.split('=')
        hashValue = explodedHashValue[1]
        responseDataString = "|".join(implodedResp) 
        generatedHash = sha1(responseDataString.encode()).hexdigest()

        if generatedHash == hashValue:
            return decryptResponse
        else:
            return 'ERROR064'
