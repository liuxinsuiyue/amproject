import pytest


@pytest.fixture(params=[1,2,3,'linda'])
def test_data(request):
    return request.param

class TestDemo:
    def test_one(self,test_data):
     print("\n test data:%s"% test_data)

    # 测试用例2  ：不需要提前登录
    def test_case2(self):
        print("测试用例2")

    def test_case3(self):
        print("测试用例3")

    def test_case4(self):
        print("测试用例4")