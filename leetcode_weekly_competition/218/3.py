class Solution:
    def concatenatedBinary(self, n: int) -> int:
        if n == 1:return 1
        dp = []

        # 十进制整数转二进制
        def decToBin(num):
            arry = []  # 定义一个空数组，用于存放2整除后的商
            while True:
                arry.append(str(num % 2))  # 用列表的append方法追加
                num = num // 2  # 用地板除求num的值
                if num == 0:  # 若地板除后的值为0，那么退出循环
                    break

            return "".join(arry[::-1])  # 列表切片倒叙排列后再用join拼接

        # 二进制整数转十进制
        def binToDec(binary):
            result = 0  # 定义一个初始化变量，后续用于存储最终结果
            for i in range(len(binary)):
                # 利用for循环及切片从右至左依次取出，然后再用内置方法求2的次方
                result += int(binary[-(i + 1)]) * pow(2, i)

            return result

        for i in range(1, n+1):
            item = decToBin(i)
            dp.append(item)
        ans = "".join(dp)
        return binToDec(ans)%1000000007

solu = Solution()
ans = solu.concatenatedBinary(12)
print(ans)
