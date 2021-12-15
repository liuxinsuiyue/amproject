import pytest

@pytest.fixture(autouse="true")
def myfixture():
    print("this is my fixture")


class TestAutoUse:
    def test_one(self):
        print("开始执行 test_one 方法")
        assert 1 + 2 == 3

    def test_two(self):
        print("开始执行 test_two 方法")
        assert 1 == 1


    def test_three(self):
        print("开始执行 test_three 方法")
        assert 1 +1 == 2
