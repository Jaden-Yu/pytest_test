'''
    设置配置信息
'''
class TestHost():
    login_host = ''

class User():   
    phone = ''
    password = ''
    login_headers = dict(referer=TestHost.login_host +'')
    enterprise_headers = dict(referer=TestHost.login_host +'')
    enter_company_id = ''

