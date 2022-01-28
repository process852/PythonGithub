"""
    迭代器(iterator):迭代取值的工具,迭代是一个重复的过程,每一次重复都是基于上一次的结果而继续
    可迭代对象:内置有__iter__方法的对象都成为可迭代对象
    迭代器：同时内置有__iter__和__next__方法
    迭代器调用__iter__()方法得到的是自己本身

"""

"""调用可迭代对象下的__iter__()方法,会返回一个迭代器"""
# l = [1, 2, 3]
# l_iterator = l.__iter__()
# print(l_iterator)
# print(type(l_iterator))
#
# # 迭代器可以使用__next__()方法逐个取出迭代器中的元素
# print(l_iterator.__next__())
# print(l_iterator.__next__())
# print(l_iterator.__next__())
# # 取完元素，会报出StopIteration异常
# print(l_iterator.__next__())

"""利用while语句实现元素的读取"""
# l = [1, 2, 3]
# l_iterator = l.__iter__()
# while True:
#     try:
#         print(l_iterator.__next__())
#     except StopIteration:
#         break

"""调用迭代器的__iter__()方法的效果,返回迭代器本身"""
# l = [1, 2, 3]
# l_iterator = l.__iter__()
# print(l_iterator)
# l_iterators = l_iterator.__iter__()
# print(l_iterators)
# print(l_iterator is l_iterators)

"""for循环工作原理,迭代器的循环"""
l = [1, 2, 3]
for item in l:
    print(item)
