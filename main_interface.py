import os
import pytest
from data import *
from frame.pytest_frame.method.precondition_method import *
from frame.pytest_frame.method.request_method import *
from frame.pytest_frame.method.assert_method import *


class Test:
    @pytest.mark.parametrize('precondition, request_method, url, param, assert_method, expect, status_code',
                             case_interface_li)
    def test_once(self, precondition, request_method, url, param, assert_method, expect, status_code):
        """
        利用parametrize装饰器实现参数化，每次传入一条用例，进行测试。
        :param precondition: 前置条件
        :param request_method: 请求方法
        :param url: 接口地址
        :param param: 参数
        :param assert_method: 断言方法
        :param expect: 预期结果
        :param status_code: 状态码
        :return:
        """
        s, headers = do_precondition(common.split_li(precondition))
        _resp = do_request(s, request_method, url, common.new_eval(param), headers)
        do_assert(_resp, assert_method, expect, status_code)


if __name__ == '__main__':
    pytest.main(['-vs', '--html=./report.html', __file__])
    # pytest.main(['-v', '--alluredir=./report', '--clean-alluredir', __file__])
    os.system('allure generate ./report --clean')
