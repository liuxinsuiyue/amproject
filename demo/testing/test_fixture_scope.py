import pytest


@pytest.fixture(scope='function',autouse="True")
def connectDB():
    print("连接数据库操作")
    yield
    print("断开数据库操作")

class TestDemo:
    def test_case1(self,connectDB):
    # def test_case1(self):效果和上面是一样的
     print("测试用例1")

    # 测试用例2  ：不需要提前登录
    def test_case2(self):
        print("测试用例2")

    def test_case3(self):
        print("测试用例3")

    def test_case4(self):
        print("测试用例4")