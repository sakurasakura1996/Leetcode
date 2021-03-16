"""
208. 实现 Trie (前缀树)
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
示例:
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true
说明:
你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。
"""
# 实现前缀树可以用数组，因为一般都是存储字符串，所以字符个数只有26个，可以用定长数组来解决。也可以用hashmap来解决。
class Trie:
    def __init__(self):
        """
        Initialize your data structure here
        """
        self.lookup = {}

    def insert(self, word: str) -> None:
        tree = self.lookup
        for a in word:
            if a not in tree:
                tree[a] = {}
            tree = tree[a]   # 前缀树的每一个节点代表一个字符串（前缀）
        # 单词结束标志
        tree["#"] = "#"
        # print(self.lookup)

    def search(self, word: str) -> bool:
        tree = self.lookup
        for a in word:
            if a not in tree:
                return False
            tree = tree[a]
        if "#" in tree:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        tree = self.lookup
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
