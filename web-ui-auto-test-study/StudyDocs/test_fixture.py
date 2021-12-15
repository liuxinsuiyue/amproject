import pytest

@pytest.fixture()
def login():
    print("这是登录方法")
    return ('tom', '123')

@pytest.fixture()
def operate():
    print("登录后的操作")

def test_case1(login,operate):
    print(login)
    print("测试用例1，需要登录")

def test_case2():
    print("测试用例2，不需要登录")

def test_case3(login):
    print(login)
    print("测试用例3，不需要登录")