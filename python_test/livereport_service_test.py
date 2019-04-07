#coding=utf-8
import traceback as tb
import random
import string
from ApiSDKJsonClient import printJsonResponse
from sms_service_LiveReportService import sms_service_LiveReportService


if __name__ == "__main__":
    try:
        print("###########################test livereport_service begin.#################################")
        service=sms_service_LiveReportService()
        # #getKeywordLiveData
        # response=service.getKeywordLiveData({
        #     "keywordIds":[4357946883]
        # })
        # printJsonResponse(response)
        # assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        
        #getAccountLiveData
        response=service.getAccountLiveData({})
        printJsonResponse(response)
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)

        print("###########################test livereport_service end.#################################")
    except Exception as e:
        print(e)
        tb.print_exc()

