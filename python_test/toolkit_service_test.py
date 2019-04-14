#coding=utf-8
import traceback as tb
from ApiSDKJsonClient import ApiSDKJsonClient
from sms_service_ToolkitService import *

if __name__ == "__main__":
    try:
        print("###########################test toolkit_service begin.#################################")
        service =sms_service_ToolkitService()
        response = service.getOperationRecord({"startDate":'2016-07-31',"endDate":'2016-08-25',"optTypes":[1,2,3,4,5],"optLevel":1,"optContents":[]})
        print('nice')
        print(response)
        
        #printJsonResponse(response)
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        "###########################test toolkit_service end.#################################"
    except Exception as e:
        print(e)
        tb.print_exc()

