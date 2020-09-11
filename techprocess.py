 # @author     Jai Girkar.
 # @copyright  2020 STS
from TransactionRequestBean import TransactionRequestBean
from TransactionResponseBean import TransactionResponseBean
from flask import Flask, redirect, url_for, request
from datetime import date
from random import randint
import re

today =  date.today()
today_date = today.strftime("%d-%m-%Y")
key = '1496899267KMOWJE'
iv = '4782583707RRHRBR'
merchantCode ='T3348'
sceme_code = "Test"

#localhost:5000/
app = Flask(__name__)
@app.route('/',  methods=['GET'] )
def encrypt():
    merchantTxnRefNumber = str(randint(1, 1000000))
    transactionRequestBean  = TransactionRequestBean()
    transactionRequestBean.requestType = 'T'
    transactionRequestBean.merchantCode = merchantCode
    transactionRequestBean.ITC = 'NIC~TXN0001~122333~rt14154~8 mar 2014~Payment~forpayment'
    transactionRequestBean.customerName = 'test'
    transactionRequestBean.merchantTxnRefNumber = merchantTxnRefNumber
    transactionRequestBean.amount = '1.00'  
    transactionRequestBean.returnURL = 'http://localhost:5000/response'
    transactionRequestBean.s2SReturnURL = 'https://tpslvksrv6046/LoginModule/Test.jsp'
    transactionRequestBean.shoppingCartDetails = sceme_code +'_' + transactionRequestBean.amount + '_0.0'
    transactionRequestBean.txnDate = today_date
    transactionRequestBean.bankCode = '470'
    # transactionRequestBean.TPSLTxnID = '71047882'
    transactionRequestBean.TPSLTxnID = 'TXN00'+ str(randint(1, 10000))
    transactionRequestBean.custId = '19872627'
    transactionRequestBean.key = key
    transactionRequestBean.iv = iv
    transactionRequestBean.webServiceLocator = "https://www.tpsl-india.in/PaymentGateway/TransactionDetailsNew.wsdl"
    url = transactionRequestBean.getTransactionToken()
    response = transactionRequestBean.getTransactionToken()
    
    if isinstance(response, str) and re.search("^msg=", response):
        outputStr = response.replace('msg=', '')
        outputArr = outputStr.split('&')
        data = outputArr[0]
        transactionResponseBean = TransactionResponseBean()
        transactionResponseBean.responsePayload = data
        transactionResponseBean.key = key
        transactionResponseBean.iv = iv
        response = transactionResponseBean.getResponsePayload()
        return response
    elif isinstance(response, str) and re.search("^txn_status=", response):
        return response
    else:    
        return redirect(response)


@app.route('/response',  methods=["POST"] )
def decrypt():  
    data = request.values
    
    if isinstance(data, dict):
        data_str =  data['msg']

    elif isinstance(data, str) and re.search("^msg=", data):
        outputStr = data.replace('msg=', '')
        outputArr = outputStr.split('&')
        data_str = outputArr[0]
    else:
        data_str = data        

    transactionResponseBean = TransactionResponseBean()
    transactionResponseBean.responsePayload = data_str
    transactionResponseBean.key = key
    transactionResponseBean.iv = iv
    response = transactionResponseBean.getResponsePayload()
    return response



if __name__ == "__main__":
    app.run(debug=True)

                







 