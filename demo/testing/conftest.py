import pytest
import yaml

from demo.python_code.calc import Calculator


@pytest.fixture(scope='class')
def connectDB():
    print("连接数据库操作")
    yield
    print("断开数据库操作")


@pytest.fixture(scope='module')
def connectDB2():
    print("连接数据库操作")
    yield
    print("断开数据库操作")

@pytest.fixture(scope="class")
def get_calc():
    print("获取计算器实例")
    calc=Calculator()
    return calc

with open('./datas/calc.yaml') as f:
    datas = yaml.safe_load(f)['add']
    adddatas = datas['datas']
    print(adddatas)
    addids = datas['myids']
    print(addids)
@pytest.fixture(params=adddatas,ids=addids) #fixture的参数化和Parameterize参数话都可以，哪个比较熟悉就用哪个
def get_datas(request):
    data=request.param
    print(f"request.param的测试数据是：{data}")
    return data