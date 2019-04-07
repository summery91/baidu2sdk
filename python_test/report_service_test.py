#coding=utf-8
import traceback as tb
import random
import string
from ApiSDKJsonClient import printJsonResponse
from sms_service_ReportService import sms_service_ReportService

# performanceData参数 指定返回数据，取值范围在下面，根据不同的物料层级，其合法的取值范围不同
#     impression(展现)--Y，必传
#     click(点击)--Y，必传
#     ctr(点击率)
#     cost(花费)
#     cpc(平均点击价格)
#     cpm(千次展现成本)
#     position(首页平均排名)
#     conversion(网页转化)
#     bridgeconversion(商桥转化，文档里面说有，但是api里面说无效)
#     phoneConversion(电话转化)
# levelOfDetails参数 指定返回的数据层级
#     2：账户粒度
#     3：计划粒度
#     5：单元粒度
#     7：创意粒度
#     11：关键词(keywordid)粒度
#     12：关键词(keywordid)+创意粒度
#     6：关键词(wordid)粒度
# reportType参数 实时数据类型
#     2：账户
#     10：计划
#     11：单元
#     14：关键词(keywordid)
#     12：创意
#     3：地域
#     9：关键词(wordid)
#     5：二级地域报告
#     21：蹊径报告
#     38：历史数据排名报告
#     40：app 下载报告
#     41：推广电话报告
#     6：搜索词

if __name__ == "__main__":
    try:
        print("###########################test report_service begin.#################################")
        service=sms_service_ReportService()
        #getRealTimeData
        response=service.getRealTimeData({
            "realTimeRequestType":{
                "unitOfTime":5,
                "startDate":"2019-04-01 00:00:00","endDate":"2019-04-02 00:00:00",
                # # 账户报告：2和2
                # "levelOfDetails":2,"reportType":2,
                # "performanceData":["impression","click","cost","cpm","ctr","cpc","conversion"]
                # # 计划报告：3和10
                # "levelOfDetails":3,"reportType":10,
                # "performanceData":["impression","click","cost","cpm","ctr","cpc","conversion"]
                # # 单元报告：5和11
                # "levelOfDetails":5,"reportType":11,
                # "performanceData":["impression","click","cost","cpm","ctr","cpc","conversion"]
                # # 关键词报告(keywordid)：11和14
                # "levelOfDetails":11,"reportType":14,
                # "performanceData":["impression","click","cost","cpm","ctr","cpc","conversion","position"]
                # # 创意报告：7和12
                # "levelOfDetails":7,"reportType":12,
                # "performanceData":["impression","click","cost","cpm","ctr","cpc","conversion","position"]
                # 关键词报告(wordid)：6和9
                "levelOfDetails":6,"reportType":9,
                "performanceData":["impression","click","cost","cpm","ctr","cpc","conversion","position"]
                # ,"rank1ImpressionRatio","rank2ImpressionRatio","rank3ImpressionRatio","rank4To8ImpressionRatio"]
                # 地域报告(不需要)
            }
        })
        printJsonResponse(response)
        assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)

        # # getRealTimeQueryData
        # response=service.getRealTimeQueryData({
        #     "realTimeQueryRequestType":{
        #         "unitOfTime":5,
        #         "startDate":"2019-04-04 00:00:00","endDate":"2019-04-05 00:00:00",
        #         # 搜索词报告：7(或12)和6
        #         "reportType":6,"levelOfDetails":7,
        #         "performanceData":["impression","click","cost","ctr"],
        #         "number":2}})
        # printJsonResponse(response)
        # assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)

        # #getRealTimePairData
        # response=service.getRealTimePairData({"realTimePairRequestType":{"performanceData":["impression","click"],"levelOfDetails":12,"startDate":"2016-08-31 12:00:00","endDate":"2016-09-01 10:00:00","unitOfTime":5,"reportType":15}})
        # printJsonResponse(response)
        # assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)

        # #getProfessionalReportId
        # response=service.getProfessionalReportId({"reportRequestType":{"performanceData":["impression","click","cost","cpc","ctr","cpm","conversion"],"levelOfDetails":2,"startDate":"2016-08-20 12:00:00","endDate":"2016-08-31 12:00:00","unitOfTime":1,"reportType":2}})
        # printJsonResponse(response)

        # #getReportState
        # response=service.getReportState({"reportId":"f61202ebad335c46832e5a158ea4905a"})
        # printJsonResponse(response)
        # assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        # #getReportFileUrl
        # response=service.getReportFileUrl({"reportId":"f61202ebad335c46832e5a158ea4905a"})
        # printJsonResponse(response)
        # assert(response["header"]["desc"]=="success" and response["header"]["status"]==0)
        
        
        print("###########################test report_service end.#################################")
    except Exception as e:
        print(e)
        tb.print_exc()

