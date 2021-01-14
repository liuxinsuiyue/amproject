import pytest




@pytest.fixture(params=[1,2,3],ids=['result1','result2','result3'])
def login1(request):
    data = request.param
    print("获取测试数据")
    return data+1
    # 不太明白这最后一步是要干嘛

class TestDemo:
    def test_one(self,login1):
     print("测试用例1")

    # 测试用例2  ：不需要提前登录
    def test_case2(self):
        print("测试用例2")

    def test_case3(self):
        print("测试用例3")

    def test_case4(self):
        print("测试用例4")