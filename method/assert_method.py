def do_assert(resp, assert_method, expect, status_code):
    if assert_method in ('status', 'status_code'):
        if assert_status_code(resp, status_code):
            return True
        else:
            return False
    elif assert_method in ('in', 'text_in'):
        if assert_text_in(resp, expect):
            return True
        else:
            return False
    elif assert_method in ('equal', 'text_equal'):
        if assert_text_equal(resp, expect):
            return True
        else:
            return False
    elif assert_method in ('json', ):
        if assert_json_str(resp, expect):
            return True
        else:
            return False
    else:
        raise Exception('不正确的断言方法')


def assert_status_code(_resp, expect_status_code):
    assert _resp.status_code == expect_status_code


def assert_text_in(_resp, inner_text):
    assert inner_text in _resp.text


def assert_text_equal(_resp, text):
    assert _resp.text == text


def assert_json_str(_resp, inner_json):
    assert inner_json in _resp.text
