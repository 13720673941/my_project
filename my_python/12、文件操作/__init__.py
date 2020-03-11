# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/12/28 11:10
import requests,warnings
warnings.filterwarnings("ignore")


url = "https://apibranch.51shouhou.cn/api/Query/cquery"

headers = {
    "Host": "apibranch.51shouhou.cn",
    "accept": "application/json, text/plain, */*",
    "origin": "http://www.51shouhou.cn",
    "sign":"a9949d8693fd07c338ad8892c5765efe",
    "content-type": "application/json;charset=UTF-8",
    "content-length": 456,
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiYnJhbmNoMDQiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiLnvZHngrnllYbnu4QiLCJuYmYiOjE1ODI2MTQ5ODYsImV4cCI6MTU4MzgyNDU4NiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIn0.tsj9zJ0ZAjmYyYFduDckARM14zXIl1GdWnqhgQAcQTg"
	}

body = {"param":"UserGroup((Areas:'S:All';Areas:'610000'))[0,20]:{PkId,GroupName,Notice,Areas,FkOwnUserPkId,Created,Brands,Categorys,ServiceTypes,CustomerNum,AgentNum,IsRecommend[desc],FeeNum,FeeType,IsSettleManageServicefee,IsHaveWarrantMoney,RiseOrderNum,UserGroupCooperationUser(FkUserGroupPkId=@PkId,FkUserPkId='76bd5ee6-4469-4bdf-a843-e4502cc45cbb'):{PkId,JoinType,RoleType,Status},BranchShopInfo(PkId=@FkOwnUserPkId):{PkId,ShortName,BranchIcon,BranchSign},UserCollection(CollectedId=@PkId):{PkId}}"}

r = requests.post(url=url,headers=headers,json=body,verify=False)

# 获取所有的列表数据

data = r.json()["datas"]

b = []

# 遍历数据列表中所有的 [] 字符的索引
for index,nums in enumerate(data):
    if nums == []:
        b.append(index)

c = []

# 判断添加偶数位置索引的字符索引
for j in b:
    if b.index(j) % 2 == 0:
        c.append(j)

# 遍历所有偶数为的索引减16就是圈子PKID的列表位置
for i in c:
    print(data[i-16])