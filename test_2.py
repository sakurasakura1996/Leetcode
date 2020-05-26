"""
练习使用 Counter
"""
from collections import Counter

s = "aabcdegf"
a = Counter(s)
print(a)
print(type(a))

print(all(a))
# all()函数判断参数内部是否都不为空或者是否都不为0，false这种，
print(any(a))
# any()判断参数内部对象是否全部为空，全部为空则为false，否则为true


## map的使用
# map函数接受两个参数，一个是函数，一个是Iterable，map将传入的函数
# 一次作用到序列的每一个元素，并把结果作为新的Iterable返回，map函数多和
# lambda函数结合使用，

a = Counter(s)
a = a.keys()
for i in a:
    print(i)




