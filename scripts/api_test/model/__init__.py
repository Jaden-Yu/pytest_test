'''
    定义请求的session类
'''
import sys
sys.path.append('../')
from requests import Session
from configs.env import TestHost
from configs.env import User


class UserSession(Session):

    def use_request(self,menthod,url,**kwargs):
        resp = self.request(menthod,url,**kwargs)
        return resp

class LoginSession(UserSession):
    
    def login(self):
        login = self.use_request(
            'post',
            TestHost.login_host+'',
            data=dict(
                phone=User.phone,
                password=User.password
                ),
            headers=User.login_headers,
            )
        print(login.status_code)
        enterprise = self.use_request(
            'post',
            TestHost.login_host+'',
            data=dict(
                company_id = User.enter_company_id
            ),
            headers=User.enterprise_headers
        )




    
   


if __name__ == "__main__":
    
    user = LoginSession()
    user.login()

    def search():
        resp = user.use_request(
            'post',
            url = 'https://sales.tungee.com/api/advance-search',
            data={'filter':'{"must":[{"hasMobile":[{"exist":"1"}]}]}','relation': '0','start': '0','end':'50','filter_lead':'1'},
            headers={'referer':'https://sales.tungee.com/customer-seeking/advanced-filter/enterprise'}
        )
        print(resp.status_code,resp.json())
    search()