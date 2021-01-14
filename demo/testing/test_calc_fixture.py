"""
以计算器实例演示如何运行单元测试框架
"""
import pytest
import yaml

from demo.python_code.calc import Calculator


class TestCalc:
    # def setup_class(self):
    #     print("开始计算")
    #     #实例化计算器
    #     self.calc = Calculator()#局部变量，前面加self.就变成实例变量;整个用来都会用到，所以定义成class级别
    #
    # def teardown_class(self):
    #     print("结束计算")


    @pytest.mark.add
    def test_add1(self,get_calc,get_datas):
        # calc = Calculator()
        # result = self.calc.add(100,100)
        result = get_calc.add(get_datas[0],get_datas[1])
        #每个测试用例都要有一个这个的判断
        # assert 200 == result
        # 浮点运算做特殊判断和处理
        if isinstance(result,float):
            result = round(result,2)
        assert get_datas[2] == result

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




