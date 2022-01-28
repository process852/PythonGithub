"""
    生成器:函数内包含yield语句，调用该函数不会立马执行内容，而是返回一个生成器
    生成器本质上是迭代器
"""

"""生成器的初步认识"""

# def func():
#     print("Hello")
#     yield 1
#     print("world")
#     yield 2
#
#
# g = func()
# print(g)  # <generator object func at 0x0000024DC3ACC6D0>
#
# # 触发函数代码运行，碰到yield语句停下来,将yield后的值返回
# re1 = g.__next__()
# print(re1)  # 1
# # 下次执行时，从上一次yield语句处开始继续执行
# re2 = g.__next__()  # 2
# print(re2)
#
# # 取完值后报出StopIteration异常
# re3 = g.__next__()
# print(re3)

"""内置方法实现生成器取值"""

# def func():
#     print("Hello")
#     yield 1
#     print("world")
#     yield 2
#
#
# g = func()
#
# next(g)  # 等价于g.__next__()
# next(g)

"""生成器的小应用,实现自定义的range"""


def myrange(start, end, step=1):
    while start < end:
        yield start
        start += step


for item in myrange(1, 10, 3):
    print(item)
