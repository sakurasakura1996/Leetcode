class Solution:
    def intToRoman(self, num: int) -> str:
        num_dict = {1:'I',
                    5:'V',
                    10:'X',
                    50:'L',
                    100:'C',
                    500:'D',
                    1000:'M',
                    4:'IV',
                    9:'IX',
                    40:'XL',
                    90:'XC',
                    400:'CD',
                    900:'CM'}
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ans = ""
        while num > 0:
            for item in nums:
                if num >= item:
                    ans += num_dict[item]
                    num -= item
                    break
        return ans

if __name__ == '__main__':
    solu = Solution()
    num = 1994
    ans = solu.intToRoman(num)
    print(ans)