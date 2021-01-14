"""
以计算器实例演示如何运行单元测试框架，
作业贴 答案会公布在课程帖/作业贴
根据等价类，边界值，因果图测试方法补全测试用例
测试用例中添加断言，验证结果
灵活使用setup(),teardown(),set_class(),teardown_class()
"""
"""
1、补全计算器（加减乘除）的测试用例
2、使用fixture，完成加减乘除用例的自动生成
3、修改测试用例的收集规则，执行所有以check_开头和test_开头的测试用例
4、创建Fixture方法实现执行测试用例前打印【开始计算】，执行测试用例之后答应【计算结束】
5、将Fixture方法存放在conftest.py,设置scope=module

"""
import pytest
import yaml

from demo.python_code.calc import Calculator

"""
这种写法load两次会导致第二次load的时候出异常
with open('./datas/calc.yaml') as f:
    adddatas = yaml.safe_load(f)['add']['datas']
    print(adddatas)
    addids = yaml.safe_load(f)['add']['myids']
    print(addids)
"""
with open('./datas/calc2.yaml') as f:
    datas = yaml.safe_load(f)['add']
    adddatas = datas['datas']
    print(adddatas)
    addids = datas['myids']
    print(addids)

class TestCalc:
    def setup_class(self):
        print("开始计算")
        #实例化计算器
        self.calc = Calculator()#局部变量，前面加self.就变成实例变量;整个用来都会用到，所以定义成class级别

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.add
    def test_add(self):
        # #实例化计算器
        # calc = Calculator()
        #调用它的add()方法
        result = self.calc.add(1,1)
        #每个测试用例都要有一个这个的判断
        assert 2 == result #equal判断两个地址 ==用来判断两个值

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect',adddatas,ids=addids)
    # ids参数增加可读性(给每一条用例重新命名，没配置就会直接显示参数化的数据)
    def test_add1(self,a,b,expect):
        # calc = Calculator()
        # result = self.calc.add(100,100)
        result = self.calc.add(a,b)
        #每个测试用例都要有一个这个的判断
        # assert 200 == result
        # 浮点运算做特殊判断和处理
        if isinstance(result,float):
            result = round(result,2)
        assert expect == result

    @pytest.mark.add
    def test_add2(self):
        # calc = Calculator()
        result = self.calc.add(0.1,0.1)
        #每个测试用例都要有一个这个的判断
        # assert 0.2 == result 可能出现不等的情况
        assert 0.2 == round(result,2) #四舍五入的方式，取两位？？

    @pytest.mark.add
    def test_add3(self):
        # calc = Calculator()
        result = self.calc.add(-1,-1)
        #每个测试用例都要有一个这个的判断
        assert -2 == result

    @pytest.mark.div
    def test_div(self):
        # calc = Calculator()
        result = self.calc.div(1,1)
        #每个测试用例都要有一个这个的判断
        assert 1 == result
    @pytest.mark.div
    def test_div2(self):
        # calc = Calculator()
        result = self.calc.div(-1,1)
        #每个测试用例都要有一个这个的判断
        assert -1 == result




