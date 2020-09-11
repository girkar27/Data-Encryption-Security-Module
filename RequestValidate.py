class RequestValidate:
    BLANK_REQUEST_TYPE = 'ERROR008'
    INVALID_REQUEST_TYPE = 'ERROR002'
    BLANK_MER_CODE = 'ERROR027'
    INVALID_KEY = 'ERROR067'
    INVALID_IV = 'ERROR068'
    BLANK_PG_RESPONSE = 'ERROR069'
    
    requestTypes = ['T','S','O','R','TIC','TIO','TWC','TRC','TCC','TWI'] 

    def isBlankOrNull(self , param = None):
        if not param or param == "NA":
            return True
        else:
            return False

    def validateRequestParam(self, requestParams = {}):
        if requestParams['pReqType'] == None or self.isBlankOrNull(requestParams['pReqType']):  #'pReqType'
            print(self.BLANK_REQUEST_TYPE)  
        
        elif requestParams['pReqType'] not in self.requestTypes:   #'pReqType'
            print(self.INVALID_REQUEST_TYPE)

        if requestParams['pMerCode'] == None or self.isBlankOrNull(requestParams['pMerCode']):  #'pMerCode'
            print(self.BLANK_MER_CODE)  
        
        if requestParams['pEncKey'] == None or self.isBlankOrNull(requestParams['pEncKey']):  #'pEncKey'
            print(self.INVALID_KEY)

        if requestParams['pEncIv'] == None or self.isBlankOrNull(requestParams['pEncIv']):  #'pEncIv'
            print(self.INVALID_IV)  
        return False

    def validateResponseParam(self, responseParams={}):
        if responseParams['pRes'] == None or self.isBlankOrNull(responseParams['pRes']):  #'pMerCode'
            print(self.BLANK_PG_RESPONSE)  
        
        if responseParams['pEncKey'] == None or self.isBlankOrNull(responseParams['pEncKey']):  #'pEncKey'
            print(self.INVALID_KEY)

        if responseParams['pEncIv'] == None or self.isBlankOrNull(responseParams['pEncIv']):  #'pEncIv'
            print(self.INVALID_IV)  
        return False






