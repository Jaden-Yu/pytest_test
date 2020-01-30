'''
    登录系统
'''
import sys
sys.path.append('env.py')

from configs import env
from configs.env import TestHost
from configs.env import User

class UserLogin():
    def __init__(self,session):
        self.user = session

    def login(self):
        login = self.user.request(
            'post',
            TestHost.login_host+'',
            data=dict(
                phone=TgUser.phone,
                password=User.password
                ),
            headers=User.login_headers,
            )
        enterprise = self.user.request(
            'post',
            TestHost.login_host+'',
            data=dict(
                company_id = User.enter_company_id
            ),
            headers=User.enterprise_headers
        )


