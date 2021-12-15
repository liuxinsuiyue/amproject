import pytest


@pytest.fixture(params=[1,2,3],ids=['result1','result2','result3'])
def login(request):
    data = request.param
    print(f"获取到测试数据: {data}")
    # return data

class TestDemo:

    # 测试用例1  ：需要提前登录
    def test_case1(self,login):
     print("测试用例1")

    # 测试用例2  ：不需要提前登录
    def test_case2(self):
        print("测试用例2")

    def test_case3(self):
        print("测试用例3")
