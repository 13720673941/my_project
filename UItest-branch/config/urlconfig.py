# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/9 9:30

"""
系统各个页面的路由
"""

# 登录页面的url
login_url = 'http://www.51shouhou.cn/singleBranch/#/login'

# 修改密码页面url
alter_pwd_url = 'http://www.51shouhou.cn/singleBranch/#/changePassword'

# 创建工单页面url
create_order_url = 'http://www.51shouhou.cn/singleBranch/#/order/add'

# 全部工单列表页面url
all_order_list_url = 'http://www.51shouhou.cn/singleBranch/#/order/search/allorder?tabType=全部工单'

# 服务中全部订单列表url
servicing_order_list_url = 'http://www.51shouhou.cn/singleBranch/#/order/search/servicing?tabType=全部工单'

# 待回访订单列表页url
wait_visit_order_url = 'http://www.51shouhou.cn/singleBranch/#/order/search/waitvisit?tabType=全部工单'

# 待返单url
wait_return_url = 'http://www.51shouhou.cn/singleBranch/#/order/search/waitvisit?tabType=待返单&page=1'

# 已返单url
finish_return_url = 'http://www.51shouhou.cn/singleBranch/#/order/search/waitvisit?tabType=已返单&page=1'

# 师傅待结算订单页面
master_wait_settle_url = 'http://www.51shouhou.cn/singleBranch/#/order/search/waitsettle?'\
                         'tabType=师傅工单结算&SubtabType=待结算&page=1'

# 服务商待结算订单页面
branch_wait_settle_url = 'http://www.51shouhou.cn/singleBranch/#/order/search/waitsettle?'\
                         'tabType=服务商工单结算&SubtabType=待结算&page=1'

# 代结算订单列表页
return_settle_url = 'http://www.51shouhou.cn/singleBranch/#/order/search/branchreturn?'\
                        'tabType=代结待结算&page=1'

# 代报单订单列表页面
instead_order_list_url = 'http://www.51shouhou.cn/singleBranch/# /order/search/instead'

# 合作网点列表页url
teamwork_branch_list_url = 'http://www.51shouhou.cn/singleBranch/#/customer/list'