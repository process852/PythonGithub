"""
    装饰器原理
    功能：在不改变原有函数基础上，添加新的功能。即在代码动态运行期间增加功能
    本质：返回函数的高阶函数
    语法：
        def 装饰器函数名(func):
            def wrapper(*args,**kwargs):
                添加新功能
                func(*args,**kwargs)
            return wrapper
        @装饰器函数名
        def func():
            函数体
    相关知识：
        函数也是一个对象，函数对象可以被赋值
        函数对象可以使用`__name__`属性拿到函数名
"""

"""原始函数实现打印日期的功能"""

# def now():
#     print("2022-1-27")


"""设计需求，不改变原有函数的内容，增加调用函数的输出显示"""

# # 首先定义一个装饰器函数
# def log(func):
#     """
#     :param func: 传入要增加新功能的函数名作为参数
#     :return: 返回添加新功能后的函数
#     """
#     def wrapper(*args, **kwargs):
#         print("call {}():".format(func.__name__))
#         func(*args, **kwargs)
#
#     return wrapper
# def now():
#     print("2022-1-27")
#
# # 将原有函数名作为log函数参数传入,使用变量接收返回值
# now = log(now)
# """输出
# call now():
# 2022-1-27
# """
# now()

"""python内部提供@语法，实现`now = log(now)的功能`,为此可以简化上述代码"""

# def log(func):
#     """
#     :param func: 传入要增加新功能的函数名作为参数
#     :return: 返回添加新功能后的函数
#     """
#
#     def wrapper(*args, **kwargs):
#         print("call {}():".format(func.__name__))
#         func(*args, **kwargs)
#
#     return wrapper
#
#
# @log  # 等价于now = log(now)
# def now():
#     print("2022-1-27")
#
# now()

"""装饰器本身需要传入参数的情况"""


def log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("{} {}():".format(text, func.__name__))
            func(*args, **kwargs)

        return wrapper

    return decorator


"""
    @log('execute') 等价于 new = log('execute')(now)
    log('execute') 返回decorator
    decorator(now) 返回wrapper
"""


@log('execute')
def now():
    print("2022-1-27")


now()
