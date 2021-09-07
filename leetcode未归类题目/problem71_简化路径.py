class Solution:
    def simplifyPath(self, path: str) -> str:
        # 首先，path是Unix风格的路径，左右结尾都是斜杠，我们是否可以根据斜杠split完再说。
        path += '/'
        paths = path.split('/')[1:-1]
        ans = []
        print(paths)
        for i, item in enumerate(paths):
            if not item or item == '.':
                continue
            elif item == '..':
                if ans:
                    ans.pop()
            else:
                ans.append(item)
        return '/' + '/'.join(ans)


if __name__ == '__main__':
    solu = Solution()
    path = "/a//b////c/d//././/.."  # 尼玛我还以为unix路径末尾必须要有 斜杠呢
    ans = solu.simplifyPath(path)
    print(ans)

