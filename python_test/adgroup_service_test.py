#coding=utf-8
import traceback as tb
import random
import string
from ApiSDKJsonClient import ApiSDKJsonClient
from sms_service_AdgroupService import *
CAMPAIGNID = 66779620
MAXPRICE=30
IDTYPE = 5
def random_name():
    return "".join(random.sample(['a','b','c','d','e','f','g','h','i','j','k','l','m','n'], 12)).replace(" ","")
def parse_ids(datas):
    ids=[]
    for data in datas:
        ids.append(data["adgroupId"])
    return ids
if __name__ == "__main__":
    try:
        print("###########################test adgroup_service begin.#################################")
        r_name=random_name()
        service =sms_service_AdgroupService()
        #addAdgroup
        response = service.addAdgroup({"adgroupTypes":[{"adgroupName":r_name,"campaignId":CAMPAIGNID,"maxPrice":MAXPRICE}]})
        print(response)
        #assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        datas=response["body"]["data"]
        #getAdgroup
        ids=parse_ids(datas)
        response=service.getAdgroup({"adgroupFields":["adgroupName", "adgroupId"],"ids":ids,"idType":IDTYPE}) 
        #assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        datas=response["body"]["data"]
        #updateAdgroup
        for data in datas:
            data["adgroupName"]=random_name()
        response=service.updateAdgroup({"adgroupTypes":datas})
        #assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        #deleteAdgroup
        ids=parse_ids(datas)
        response=service.deleteAdgroup({"adgroupIds":ids})
        #assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        #printJsonResponse(response)
        print("###########################test adgroup_service end.#################################")
    except Exception as e:
        print(e)
        tb.print_exc()

