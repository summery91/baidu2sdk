#coding=utf-8
import traceback as tb
import random
import string
from sms_service_KeywordService import sms_service_KeywordService,printJsonResponse
ADGROUPID = 2028778327
IDTYPE = 11
ISTMP = 0
def random_name():
    return "".join(random.sample(['a','b','c','d','e','f','g','h','i','j','k','l','m','n'], 12)).replace(" ","")
def parse_ids(datas):
    ids=[]
    for data in datas:
        ids.append(data["keywordId"])
    return ids
if __name__ == "__main__":
    try:
        print("###########################test keyword_service begin.#################################")
        r_name=random_name()
        service =sms_service_KeywordService()
        #addWord
        response = service.addWord({"keywordTypes":[{"keyword":r_name,"adgroupId":ADGROUPID}]})
        printJsonResponse(response)
        # assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        datas=response["body"]["data"]
        #getWord
        ids=parse_ids(datas)
        response=service.getWord({"wordFields":["keyword", "keywordId"],"idType":IDTYPE,"ids":ids,"getTemp":ISTMP}) 
        printJsonResponse(response)
        # assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        datas=response["body"]["data"]
        #updateWord
        for data in datas:
            data["keyword"]=random_name()
        response=service.updateWord({"keywordTypes":datas})
        printJsonResponse(response)
        # assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        #deleteWord
        ids=parse_ids(datas)
        response=service.deleteWord({"keywordIds":ids})
        # assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        printJsonResponse(response)
        print("###########################test keyword_service end.#################################")
    except Exception as e:
        print(e)
        tb.print_exc()

