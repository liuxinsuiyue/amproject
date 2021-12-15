import pytest

"""
parametrize
"""

@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+5",7),("7*5",30)])
def test_eval(test_input,expected):
    assert eval(test_input) == expected
    # eval 将字符串str当成有效的表达式来求值
    # 整个执行过程中，pytest 将参数列表 [("3+5",8),("2+5",7),("7*5",30)] 中的三组数据取出来，每组数据生成一条测试用例，并且将每组数据中的两个元素分别赋值到方法中，作为测试方法的参数由测试用例使用。
"""
多次使用 parametrize
"""
@pytest.mark.parametrize('x',[1,2])
@pytest.mark.parametrize('y',[8,10,11])
def test_foo(x,y):
  print(f"测试数据组合x: {x},y: {y}")
  """
  分析如上运行结果，测试方法  test_foo()  添加了两个 @pytest.mark.parametrize()装饰器，两个装饰器分别提供两个参数值的列表，2 * 3 = 6种结合，
  pytest便会生成 6条测试用例。在测试中通常使用这种方法是所有变量、所有取值的完全组合，可以实现全面的测试。
  """


"""
fixture和parametrize组合
"""
test_user_data = ['Tom', 'Jerry']

@pytest.fixture(scope="module")
def login_r(request):
    # 通过request.param获取参数
    user = request.param
    print(f"\n 登录用户： {user}")
    return user

#方法名作为参数 在使用parametrize的时候添加一个参数indirect=true,login_r 会被作为函数去执行，test_user_data 被当作参数传入到 login_r 方法中，生成多条测试用例。通过 return 将结果返回，当调用 login_r 可以获取到 login_r 这个方法的返回数据。
@pytest.mark.parametrize("login_r", test_user_data,indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例中 login 的返回值: {a}")
    assert a != ""
    print("fixture会被多次调用")