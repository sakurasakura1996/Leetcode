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



a = 'a'
b = 'c'
# print(b-a)
# python中字符通过ascii相减不像c++可以直接减，可以通过ord()传入一个字符转换成对应的ascii值

print(ord(a)-ord(b))

print("----测试整数相除-----")
a = 12
b = 2
# print(a/b)
print(type(a))

ans = a/b
print(type(ans))
print(ans)
print(round(float(a)/b,3))


print("-----")
for i in range(101, 101):
    print(i)

print("----测试")
import datetime
start = datetime.datetime.now()
ans = [0 for i in range(1000000)]
end = datetime.datetime.now()
print("time"+str(end-start))
start = datetime.datetime.now()
ans = [0] * 10000
end = datetime.datetime.now()
print("time"+str(end-start))


print("----test set")
a = set([-1,0,1])
print(a)

print("----test sort")
nums = [0, 4, 5, 3]
nums.sort()
print(nums)


print("----str sort")
string = ['a','c','b','a']
string.sort()
print(string)

print("---循环")
for i in range(5):
    if i == 3:
        break
    print(i)


print("---index and find")
nums = [3, 4, 6, 6, 5, 3]
a = nums.index(3)  # index只能直到首次出现该字母的位置
print(a)

print("----test 二维数组")
dp = [[0] * 3]*3
print(dp)
dp[1][1] = 1   # 这里要特别注意，我只改了一个地方的值，然而dp数组中的三个地方都改动了，说明他们是共享内存的呀，所以以后要注意这里。
print(dp)
print(type(dp))

print("---np list")
import numpy as np
dp = list(np.zeros((3,3),dtype=np.int))
print(type(dp))
print(dp)
dp[1][1] = 1
print(dp)

print("test split")
s = "1-401--349---90--88"
ans = s.split("-")
print(ans)
ans.remove('')
print(ans)

a = [2,2]
posi = [a]
print(posi)
posi.append([3,3])
print(posi)
print([3,3] in posi)

print("___测试列表共享内存")
a = [1,2,3]
b = []
b.append(a)
print(b)
a.clear()
print(b)
# 还真是共享的内存。

print("----测试list.copy()是否共享内存")
a = [1,2,3]
b = a.copy()
print(b)
a.clear()
print(b)
# copy并不共享内存
c = b
print(c)
b.clear()
print(c)
# 直接令c = b也是共享内存的
