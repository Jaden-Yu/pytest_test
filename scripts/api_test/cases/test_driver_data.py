import sys

sys.path.append('../')

import pytest
import json
import configs.env

from model.case_to_excel import open_case_excel
from model import UserSession, LoginSession
from configs.user_login import UserLogin

user = LoginSession()


@pytest.mark.parametrize(
    'menthod,url,test_params,test_data,test_headers',
    [i for i in open_case_excel()]
)
def test_case(menthod, url, test_params, test_data, test_headers):
    params = None if None == test_params else eval(test_params)
    data = None if None == test_data else eval(test_data)
    headers = None if None == test_headers else eval(test_headers)
    resp = user.use_request(menthod=menthod, url=url, params=params, data=data, headers=headers)

    assert resp.status_code == 200
