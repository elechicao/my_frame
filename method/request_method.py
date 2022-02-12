import json


def do_request(session_obj, request_method, url, param, headers):
    # try:
    #     resp = eval(f'{request_method}({session_obj}, {url}, {param}, {headers})')
    #     print('_____________________', resp)
    #     return resp
    # except Exception as e:
    #     print('请求方法错误', e)

    if request_method in ('GET', 'get'):
        resp = GET(session_obj, _url=url, _param=param, _headers=headers)
        return resp
    elif request_method in ('POST', 'post'):
        resp = POST(session_obj, _url=url, _param=param, _headers=headers)
        return resp
    elif request_method in ('post_json', 'POST_JSON'):
        resp = POST_JSON(session_obj, _url=url, _param=param, _headers=headers)
        return resp
    else:
        raise Exception('不正确的请求方法')


def GET(session_obj, _url, _param, _headers):
    """
    GET请求
    :param session_obj:
    :param _url:
    :param _param:
    :param _headers:
    :return:
    """
    _resp = session_obj.get(url=_url, params=_param, headers=_headers)
    return _resp


def POST(session_obj, _url, _param, _headers):
    """
    POST请求
    :param session_obj:
    :param _url:
    :param _param:
    :param _headers:
    :return:
    """
    _resp = session_obj.post(url=_url, data=_param, headers=_headers)
    return _resp


def POST_JSON(session_obj, _url, _param, _headers):
    """
    POST请求
    :param session_obj:
    :param _url:
    :param _param:
    :param _headers:
    :return:
    """
    _resp = session_obj.post(url=_url, json=json.loads(_param), headers=_headers)
    return _resp
