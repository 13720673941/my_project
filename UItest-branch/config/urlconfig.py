# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/9 9:30

"""
系统各个页面的路由
"""

# 正式host地址
official_host = 'http://www.51shouhou.cn'

# 测试地址host地址
test_host = 'http://test.super.com.cn'

# 登录页面的url
login_url = official_host+'/singleBranch/#/login'

# 网点首页预览页Url
review_url = official_host+'/singleBranch/#/overview/index'

# 修改密码页面url
alter_pwd_url = official_host+'/singleBranch/#/changePassword'

# 创建工单页面url
create_order_url = official_host+'/singleBranch/#/order/add'

# 全部工单列表页面url
all_order_list_url = official_host+'/singleBranch/#/order/search/allorder?tabType=全部工单&SubtabType=待结算&page=1'

# 服务中全部订单列表url
servicing_order_list_url = official_host+'/singleBranch/#/order/search/servicing?tabType=全部工单'

# 待回访订单列表页url
wait_visit_order_url = official_host+'/singleBranch/#/order/search/waitvisit?tabType=全部工单'

# 待返单url
wait_return_url = official_host+'/singleBranch/#/order/search/waitvisit?tabType=待返单&page=1'

# 已返单url
finish_return_url = official_host+'/singleBranch/#/order/search/waitvisit?tabType=已返单&page=1'

# 师傅待结算订单页面
master_wait_settle_url = official_host+'/singleBranch/#/order/search/waitsettle?'\
                         'tabType=师傅工单结算&SubtabType=待结算&page=1'

# 服务商待结算订单页面
branch_wait_settle_url = official_host+'/singleBranch/#/order/search/waitsettle?'\
                         'tabType=服务商工单结算&SubtabType=待结算&page=1'

# 代结算订单列表页
return_settle_url = official_host+'/singleBranch/#/order/search/branchreturn?'\
                        'tabType=代结待结算&page=1'

# 代报单订单列表页面
instead_order_list_url = official_host+'/singleBranch/# /order/search/instead'

# 合作网点列表页url
teamwork_branch_list_url = official_host+'/singleBranch/#/customer/list'

# 客户统计页面url
customer_statistics_url = official_host+'/singleBranch/?#/customer/statistics'

# 合作消息列表页面
teamwork_news_list_url = official_host+'/singleBranch/#/customer/coopApplication'

# 师傅列表页面
master_list_url = official_host+'/singleBranch/#/master/index/index'

# 师傅工单统计页面url
master_order_statistics_url = official_host+'/singleBranch/#/master/masterOrder/index'

# 网点单量记录页面url
master_order_number_url = official_host+'/singleBranch/#/operate/orderLog/index'

# 短信发送记录页面url
short_msg_log_url = official_host+'/singleBranch/#/operate/noteLog/index'

# 我的支出页面Url
my_income_url = official_host+'/singleBranch/#/finance/brincome/income'

# 我的支出页面url
my_expend_url = official_host+'/singleBranch/#/finance/brincome/outgoing'

# 我的钱包页面
my_wallet_url = official_host+'/singleBranch/#/finance/wallet'

# 备件公司库存页面
company_inventory_url = official_host+'/singleBranch/#/sparepart/stock/company'

# 备件师傅领用记录页面
master_receive_log_url = official_host+'/singleBranch/#/sparepart/stock/retrievalRecord'

# 备件库存调整记录页面
inventory_adjust_url = official_host+'/singleBranch/#/sparepart/stock/IORecord'

# 待返厂页面
wait_return_factory_url = official_host+'/singleBranch/#/sparepart/returnFactory/waitReturn'