from RequestValidate import RequestValidate
import time
from hashlib import sha1
from AES import AES_en
from zeep import Client
import socket

class TransactionRequestBean(RequestValidate):

    tilda = "~"

    separator = "|"

    requestType= ""

    merchantCode = ""

    merchantTxnRefNumber = ""

    ITC = ""

    amount = ""

    accountNo = ""

    currencyCode = ""

    uniqueCustomerId = ""

    returnURL = ""

    s2SReturnURL = ""

    TPSLTxnID = ""

    shoppingCartDetails = ""

    txnDate = ""

    email = ""

    mobileNumber = "8451053257"

    socialMediaIdentifier = ""

    bankCode = ""

    customerName = ""

    reqst = None

    webServiceLocator = "NA"

    MMID = "1231221"

    OTP = "123123"

    key= None #####

    iv= None#####

    mkd= None #####

    mode = 2

    logPath = ""

    currDate = None ######

    rqst_kit_vrsn = 1

    custId = ""

    cardId = "1234"

    cardNo = '4111111111111111'

    cardName = 'dheeraj'

    cardCVV = "123"

    cardExpMM = "11"

    cardExpYY = "25"

    timeOut = 30

    def __set(self, field, value):
        self.field = value

    def __get(self, variable):
        return self.variable

    def getTilda(self):
        return self.tilda

    def getseparator(self):
        return self.separator

    def getUniqueCustomerId(self):
        return self.uniqueCustomerId

    def getEmail(self):
        return self.email

    def getSocialMediaIdentifier(self):
        return self.socialMediaIdentifier

    def getReqst(self):
        return self.reqst

    def getWebServiceLocator(self):
        return self.getWebServiceLocator

    def getMkd(self):
        return self.mkd

    def getBlockSize(self):
        return self.blockSize

    def getMode(self):
        return self.mode

    def getLogPath(self):
        return self.logPath


    def getCurrDate(self):
        return self.currDate

    def getRqst_kit_vrsn(self):
        return self.rqst_kit_vrsn

    def getTimeOut(self):
        return self.timeOut

    def setTilda(self, tilda):
        self.tilda = tilda

    def setUniqueCustomerId(self, uniqueCustomerId):
        self.uniqueCustomerId = uniqueCustomerId

    def setEmail(self,  email):
        self.email = email
   
    def setSocialMediaIdentifier(self, socialMediaIdentifier):
        self.socialMediaIdentifier = socialMediaIdentifier

    def setReqst(self, reqst):
        self.reqst = reqst

    def setWebServiceLocator(self, webServiceLocator):
        self.webServiceLocator = webServiceLocator

    def setMkd(self, mkd): 
        self.mkd = mkd

    def setBlockSizes(self, blockSize):
        self.blockSize = blockSize

    def setMode(self, mode):
        self.mode = mode

    def setLogPath(self, logPath):
        self.logPath = logPath

    def setCurrDate(self, currDate):
        self.currDate = currDate

    def setRqst_kit_vrsn(self, rqst_kit_vrsn):
        self.rqst_kit_vrsn = rqst_kit_vrsn

    def getEncryptedData(self):
        clientMetaData = ""

        if  not self.isBlankOrNull(self.ITC):
            
            clientMetaData = clientMetaData + "{itc:" + self.ITC + "}"                
        

        if  not self.isBlankOrNull(self.email):
        
            clientMetaData = clientMetaData + "{email:" + self.email + "}"                
        

        if  not self.isBlankOrNull(self.mobileNumber):
            
            clientMetaData = clientMetaData + "{mob:" + self.mobileNumber + "}"                
            

        if  not self.isBlankOrNull(self.uniqueCustomerId):
            
            clientMetaData = clientMetaData + "{custid:" + self.uniqueCustomerId + "}"                
        
        
        if  not self.isBlankOrNull(self.customerName):
            
            clientMetaData = clientMetaData + "{custname:" + self.customerName + "}"                
            
            
        self.strReqst = ""
        
        if not self.isBlankOrNull(self.requestType):
            self.strReqst = self.strReqst + "rqst_type=" + self.requestType

        self.strReqst = self.strReqst + "|rqst_kit_vrsn=1.0." + str(self.rqst_kit_vrsn)
        
        if not self.isBlankOrNull(self.merchantCode):
            self.strReqst = self.strReqst + "|tpsl_clnt_cd=" + self.merchantCode
            


        if not self.isBlankOrNull(self.accountNo): 
            self.strReqst = self.strReqst + "|accountNo=" + self.accountNo
            

        if not self.isBlankOrNull(self.merchantTxnRefNumber): 
            self.strReqst = self.strReqst + "|clnt_txn_ref=" + self.merchantTxnRefNumber
            

        if not self.isBlankOrNull(clientMetaData): 
            self.strReqst = self.strReqst + "|clnt_rqst_meta=" + clientMetaData
            


        if not self.isBlankOrNull(self.amount): 
            self.strReqst = self.strReqst + "|rqst_amnt=" + self.amount
        

        if not self.isBlankOrNull(self.currencyCode):
            self.strReqst = self.strReqst + "|rqst_crncy=" + self.currencyCode
        

        if not self.isBlankOrNull(self.returnURL):
            self.strReqst = self.strReqst + "|rtrn_url=" + self.returnURL
        

        if not self.isBlankOrNull(self.s2SReturnURL):
            self.strReqst = self.strReqst + "|s2s_url=" + self.s2SReturnURL
        

        if not self.isBlankOrNull(self.shoppingCartDetails):
            self.strReqst = self.strReqst + "|rqst_rqst_dtls=" + self.shoppingCartDetails
        
        if not self.isBlankOrNull(self.txnDate): 
            self.strReqst = self.strReqst + "|clnt_dt_tm=" + self.txnDate
        

        if not self.isBlankOrNull(self.bankCode):
            self.strReqst = self.strReqst + "|tpsl_bank_cd=" + self.bankCode
        

        if not self.isBlankOrNull(self.TPSLTxnID): 
            self.strReqst = self.strReqst + "|tpsl_txn_id=" + self.TPSLTxnID
        

        if not self.isBlankOrNull(self.custId):
            self.strReqst = self.strReqst + "|cust_id=" + self.custId
        

        if not self.isBlankOrNull(self.cardId): 
            self.strReqst = self.strReqst + "|card_id=" + self.cardId
        

        if not self.isBlankOrNull(self.mobileNumber):
            self.strReqst = self.strReqst + "|mob=" + self.mobileNumber

        if self.requestType == "TWC" or self.requestType == "TRC" or self.requestType == "TIC":
            cardInfoBuff = ""
            cardInfoBuff = cardInfoBuff + "card_Hname=" + self.cardName
            cardInfoBuff = cardInfoBuff + "|card_no=" + self.cardNo
            cardInfoBuff = cardInfoBuff + "|card_Cvv=" + self.cardCVV
            cardInfoBuff = cardInfoBuff + "|exp_mm=" + self.cardExpMM
            cardInfoBuff = cardInfoBuff + "|exp_yy=" + self.cardExpYY
            aes = AES_en(cardInfoBuff, self.key, self.mode, self.iv)
            aes.require_pkcs5()
            cardInfoStr = aes.encryptHex()
            aesObj = AES_en(cardInfoStr, self.key, self.mode, self.iv)
            aesObj.require_pkcs5()
            cardInfo = aesObj.encryptHex()
            self.strReqst =  self.strReqst + "|card_details=" + cardInfo

        elif self.requestType == "TCC":
            cardInfoBuff = ""
            cardInfoBuff = cardInfoBuff + "|card_Cvv=" + self.cardCVV;
            aes = AES_en(cardInfoBuff, self.key, self.mode, self.iv)
            aes.require_pkcs5()
            cardInfoStr = aes.encryptHex()
            aesObj = AES_en(cardInfoStr, self.key, self.mode, self.iv)
            aesObj.require_pkcs5()
            cardInfo = aesObj.encryptHex()
            self.strReqst = self.strReqst + "|card_details=" + cardInfo
        
        elif self.requestType == "TWI":
            impsInfoBuff = ""
            impsInfoBuff = impsInfoBuff + "mmid=" + self.MMID
            impsInfoBuff = impsInfoBuff + "|mob_no=" + self.mobileNumber
            impsInfoBuff = impsInfoBuff + "|otp=" + self.OTP
            aes = AES_en(impsInfoBuff, self.key, self.mode, self.iv)
            aes.require_pkcs5()
            impsInfoStr = aes.encryptHex()
            aesObj = AES_en(impsInfoStr, self.key, self.mode, self.iv)
            aesObj.require_pkcs5()
            impsInfo = aesObj.encryptHex()
            self.strReqst = self.strReqst + "|imps_details=" + impsInfo

        elif self.requestType == "TIO":
            self.strReqst = self.strReqst + "|otp=" + self.OTP

        self.strReqst = self.strReqst + "|hash=" + sha1(self.strReqst.encode()).hexdigest()
        aesObj = AES_en(self.strReqst, self.key, self.mode, self.iv)
        aesObj.require_pkcs5()
        encryptedData = aesObj.encrypt()
        return encryptedData

    def getTransactionToken(self):
        socket.setdefaulttimeout(self.timeOut)
        if self.webServiceLocator != None and self.webServiceLocator != "" and self.webServiceLocator != "NA":
            params =  {}
            params['pReqType'] = self.requestType
            params['pMerCode'] = self.merchantCode
            params['pEncKey'] = self.key
            params['pEncIv'] = self.iv 
            errorResponse = self.validateRequestParam(params)
            if errorResponse:
                return errorResponse
            encryptedData = self.getEncryptedData()

            if not encryptedData: 
                return None
            post_data = encryptedData + "|" + self.merchantCode + "~"
            wsdl = self.webServiceLocator
            request_data={"trace" : 1, "exceptions": 1}
            client = Client(wsdl)
            data = {
                'msg': post_data
            }
            response = client.service.getTransactionToken(**data)
            # import pdb
            # pdb.set_trace()
            return response
        else:
            return "ERROR065"














               
            


               
                

