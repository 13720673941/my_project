# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/9 9:30

"""
    系统各个页面的路由
"""

from public.common.rwConfig import read_config_data
from config.pathConfig import *

host_number = read_config_data("Environment","environment",configPath)

# 初始化host地址
host = None
if host_number == "1":
    host = "http://www.51shouhou.cn"
elif host_number == "2":
    host = "http://test.super.com.cn"
else:
    raise NameError("'{0}' host number is error ! you can input 1、2 .".format(host_number))

# 登录页面的url
login_url = host+'/singleBranch/#/login'
# 网点首页预览页Url
review_url = host+'/singleBranch/#/overview/index'
# 修改密码页面url
alter_pwd_url = host+'/singleBranch/#/changePassword'
# 创建工单页面url
create_order_url = host+'/singleBranch/#/order/add'
# 全部工单列表页面url
all_order_list_url = host+'/singleBranch/#/order/search/allorder?tabType=全部工单&SubtabType=待结算&page=1'
# 服务中全部订单列表url
servicing_order_list_url = host+'/singleBranch/#/order/search/servicing?tabType=全部工单'
# 待抢单页面工单列表
wait_grad_order_url = host+'/singleBranch/#/order/search/waitaccept?tabType=抢单市场&SubtabType=待结算&page=1'
# 待回访订单列表页url
wait_visit_order_url = host+'/singleBranch/#/order/search/waitvisit?tabType=全部工单'
# 拒单列表页url
refuse_order_list_url = host+'/singleBranch/#/order/search/waitdispatch?tabType=拒接工单&SubtabType=待结算&page=1'
# 待返单url
wait_return_url = host+'/singleBranch/#/order/search/waitvisit?tabType=待返单&page=1'
# 已返单url
finish_return_url = host+'/singleBranch/#/order/search/waitvisit?tabType=已返单&page=1'
# 无效工单列表页
invalid_order_url = host+"/singleBranch/#/order/search/waitvisit?tabType=无效工单&SubtabType=待结算&page=1"
# 催单工单列表页
prompt_order_url = host+"/singleBranch/#/order/search/abnormal?tabType=催单工单&SubtabType=待结算&page=1"
# 师傅待结算订单页面
master_wait_settle_url = host+'/singleBranch/#/order/search/waitsettle?'\
                         'tabType=师傅工单结算&SubtabType=待结算&page=1'
# 进入工单支出页面
bill_out_going_url = host+'/singleBranch/#/finance/billOutgoing'
# 服务商待结算订单页面
branch_wait_settle_url = host+'/singleBranch/#/order/search/waitsettle?'\
                         'tabType=服务商工单结算&SubtabType=待结算&page=1'
# 代结算订单列表页
return_settle_url = host+'/singleBranch/#/order/search/branchreturn?'\
                        'tabType=代结待结算&page=1'
# 代报单订单列表页面
instead_order_list_url = host+'/singleBranch/# /order/search/instead'
# 合作网点列表页url
teamwork_branch_list_url = host+'/singleBranch/#/customer/list'
# 客户统计页面url
customer_statistics_url = host+'/singleBranch/?#/customer/statistics'
# 合作消息列表页面
teamwork_news_list_url = host+'/singleBranch/#/customer/coopApplication'
# 师傅列表页面
master_list_url = host+'/singleBranch/#/master/index/index'
# 师傅工单统计页面url
master_order_statistics_url = host+'/singleBranch/#/master/masterOrder/index'
# 网点单量记录页面url
order_log_list_url = host+'/singleBranch/#/operate/orderLog/index'
# 短信发送记录页面url
short_msg_log_url = host+'/singleBranch/#/operate/noteLog/index'
# 我的支出页面Url
my_income_url = host+'/singleBranch/#/finance/billIncome'
# 我的支出页面url
my_expend_url = host+'/singleBranch/#/finance/billOutgoing'
# 我的钱包页面
my_wallet_url = host+'/singleBranch/#/finance/wallet'
# 备件公司库存页面
company_inventory_url = host+'/singleBranch/#/sparepart/stock/company'
# 备件师傅领用记录页面
master_receive_log_url = host+'/singleBranch/#/sparepart/stock/retrievalRecord'
# 师傅库存备件页面
master_inventory_url = host+'/singleBranch/#/sparepart/stock/master'
# 备件库存调整记录页面
inventory_adjust_url = host+'/singleBranch/#/sparepart/stock/IORecord'
# 待返厂页面
wait_return_factory_url = host+'/singleBranch/#/sparepart/returnFactory/waitReturn'
# 已返厂页面
already_return_faction_url = host+'/singleBranch/#/sparepart/returnFactory/alreadyReturn'
# 用户评价页面地址-> +OrderPkId+ 替换订单PkId
user_evaluate_url = host+'/singleUser/#/sms/evaluate?pkid=+orderPkId+'
# 我创建的圈子页面
my_create_group_list = host+'/singleBranch/#/groupList/group'
# 圈子订单抢单市场地址
group_order_of_market_url = host+'/singleBranch/#/order/search/waitaccept?tabType=%E5%9C%88%E5%AD%90%E6%8A%A2%E5%8D%95' \
                                 '&SubtabType=%E5%BE%85%E7%BB%93%E7%AE%97&page=1'
# 我加入的圈子列表页面
group_list_my_join = host+'/singleBranch/#/groupList/Group/partakeGroup'
