import pytest


def test_a():
    print("test_demo.py 测试用例a")

def test_b():
    print("test_demo.py 测试用例b")

def test_c():
    assert 1 == 2

@pytest.mark.parametrize('a',[1,2,3])
@pytest.mark.parametrize('b',[4,5,6,7])
# 多个参数，笛卡尔积，生成大量用例
def test_param(self,a,b):
    print(f"a={a},b={b}")