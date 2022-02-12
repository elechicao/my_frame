import requests


def do_precondition(precondition_li):
    try:
        _s = requests.Session()
        _headers = None
        if not precondition_li:
            for precondition in precondition_li:
                _s, _headers = eval(f'{precondition}({_s}, {_headers})')
        return _s, _headers
    except Exception as e:
        print('前置方法错误', e)


def login(_s, _headers):
    """
    登录并获取session对象
    :return: session对象， 可能要用到的请求头
    """
    _param = {{"username": "admin", "password": "admin123", "verifycode": 0000}}
    _resp = _s.post('http://localhost:8081/woniusales/user/login', data=_param)
    return _s, _headers
