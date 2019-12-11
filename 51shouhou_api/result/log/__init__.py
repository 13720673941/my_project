# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/11/5 11:35

import urllib.parse
import http.client
import json,ssl,requests
import urllib.request

# ssl._create_default_https_context = ssl._create_unverified_context


# proxies = {"http":"apibranch.51shouhou.cn/api/Query/cquery","https":"apibranch.51shouhou.cn/api/Query/cquery"}

url = "https://apibranch.51shouhou.cn/api/Query/cquery"
# conn = http.client.HTTPSConnection('apibranch.51shouhou.cn:443')

headers = {
    "Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiYnJhbmNoMDEiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiLnvZHngrnllYbnu4QiLCJuYmYiOjE1NzQ1MDI0MDUsImV4cCI6MTU3NTcxMjAwNSwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIn0.RKZEmnWM5d5gtPCUuAaUmuHfB_XPkztJs34-MYw2awE",
    "Content-Type":"application/json",
    "sign":"e04721f7377d1035799e00a5c5d2312b",
    "content-length":"2558"
}

body = {"param":"MapPedInfoesRoles(1=1,(FkToUserId='75988978-5347-44f7-9f57-2838272ab5af'),IsRefused=null,IsReassigned=null,TradeStatusName!='用户下单')[0,20]:{MasterConfirmTime,MasterReserveTime,DispatchMasterTime,MasterFinishTime,ReserveTime,LatestStepTime[desc],CreateTime,SettleTime,VisitTime,ActionTime,FinalPrice,TotalPrice,PkId,TradeId,FKServiceTypePkId,ServiceTypeName,ReserveNoon,FkProductBrandPkId,BrandName,FkProductInfoPKId,ProductName,ProductModelName,FkBuyChannelPkId,BuyChannelName,GuarnteeType,FwContent,FaultType,FeedBack,InnerSerialNo,OuterSerialNo,ProductCount,BuyTime,SubmitPriceTime,IsExistReminder,TradeFrom,FkTradeFromId,IsInValid,IsFinishByBranch,InvalidType,InvalidReason,InvalidFrom,InvalidMarkTime,TradeStatusName,LatestStepName,RowId,CreatorId,Mobile,ContactName,Telephone,Province,City,Area,AreaId,AddInfo,FkMasterPkId,MasterFullName,MasterMobile,MasterReseverOptTime,MasterReservePeriod,MasterHomeTime,PayType,PayTime,,TradeSource,VendorStatus,FkWaitDispatchBranchPkId,OwnerName,OwnerId,FkToBranchPkId,TradeType,ThirdSettleMoney,CreatorName,ToBranchName,AuthCode,checkInnerSerialNo,checkInnerSerialStatus,IsFinishedThirdOrder,ThirdFinishOrderReturnData,IsUserCalcNegativeCount,IsCalcNegativeCount,FkVShopOrderId,ReserveSection,ContactSex,FkVShopOrderPkId,StatusName,FkFromUserId,FkFromUserName,FkToUserId,FkToUserName,IsReturnConfirm,IsSettled,IsVisited,IsRefused,Role_Type,RefusedReason,,NoTimeTime:datediff(minute,DATEADD(hh,CONVERT(INT,SUBSTRING(MasterReservePeriod,7,2)),MasterReserveTime),getdate()),NoacceptTime:datediff(minute,DispatchMasterTime,getdate()),NoreservationTime:datediff(minute,MasterConfirmTime,getdate()),TradeVisit(TradePkId:@PkId,"
                "FkVisitByUserId='75988978-5347-44f7-9f57-2838272ab5af'):{ServiceAttitude,SafetyEvaluation,TotalPrice,VisitPrice,VisitResult,VisitFeedBack,CreateTime[desc],VisitUserId,VisitUserName},TradeSettlement(TradePkId:@PkId):{SettleType,UserId,ToUserId,ToUserName,SettleMode,SettlePrice,SettleWay,SettleRatio,CreateTime[desc]},TradeServicePrice(FkTradePkId:@PkId):{Name[desc],Pirce},TradeComment(FkTradePkId:@PkId):{Id,CreateUserName,Content,CreateTime[desc]},TradeRolesRelation(FkTradePkId:@PkId):{Id[desc],FkFromUserId,FkToUserId,FkFromUserName,FkToUserName,Role_StepType,IsSettled,IsVisited,IsReturnConfirm,IsRefused,IsReassigned,Role_Type,VisitTime,SettleTime,RefusedReason,RolesTotalPrice,ActionTime,DispatchStatusCode},VShopOrders(PkId:@FkVShopOrderPkId):{PkId[desc],IsGroupCost,IsFound,isConpon,ConponPrice,TotalPrice,isFixedPrice,SettlementPrice,AdvancePrice,FinalPrice,isPay}}"}



r = requests.post(url,json=body,headers=headers)

print(r.status_code)

