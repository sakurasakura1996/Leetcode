"""
前面用到了defaultdict的排序作用，但是好像不太熟悉这其中的操作啊，这里来测试一下
"""

from collections import defaultdict
dic = defaultdict(list)
s = "bcabc"
for i, ch in enumerate(s):
    dic[ch].append(i)
print(dic)

# 这个时候，我想给defaultdict按照key值排序。下面我将测试一下各种我自己以为的排序方式
# way1
print("way1-----")
a = sorted(dic)
print(a)
print(type(a))
print("way2-----")
b = sorted(dic.items())
print(b)
print(type(b))
print("way3-----")
c = sorted(dic.keys())
print(c)
print(type(c))
print("way3----")
d = sorted(dic.values())
print(d)
print(type(d))
# 上面排序返回的结果都是list类型，其实不难理解，因为后面几种sorted函数中的参数都是list类型。所以排序返回的结果肯定都是list啊
# 那么我理想中的按key排序并且返回的还是dict的排序方法怎么写呢
for key in sorted(dic):
    print(key, dic[key])
# 上面这是可以得到我想要的结果。

