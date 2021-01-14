def setup_module():
    print("模块级别的setup")
def teardown_module():
    print("模块级别的teardown")

def setup_function():
    print("函数级别的setup")
def teardown_function():
    print("函数级别的teardown")

def test_func1():
    print("测试func1")


class TestDemo:
    def setup_class(self):
        print("类级别的setup")
    def teardown_class(self):
        print("类级别的teardown")
    def setup(self):
        print("方法级别的setup")
    def teardown(self):
        print("方法级别的teardown")

    def test_demo1(self):
        print("testdemo1")
    def test_demo2(self):
        print("testdemo2")

class TestDemo2:

    def test_demo21(self):
        print("testdemo21")
    def test_demo22(self):
        print("testdemo22")