#coding=utf-8
import traceback as tb
import random
import string
from ApiSDKJsonClient import *
from sms_service_SearchService import *
if __name__ == "__main__":
    try:
        print("###########################test search_service begin.#################################")
        service=sms_service_SearchService()
        #getMaterialInfo
        response=service.getCountById({"countType":3})
        printJsonResponse(response)
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        
        #getMaterialInfo
        response=service.getMaterialInfoBySearch({"searchWord":"鲜花","searchType":0,"searchLevel":2})
        printJsonResponse(response)
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)

        #getTab
        response=service.getTab({"idType":11,"tabIds":[1,2,3,4,5]})
        printJsonResponse(response)
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        print("###########################test search_service end.#################################")
    except Exception as e:
        print(e)
        tb.print_exc()

