#incorrect version
# class TrieNode:
#     def __init__(self):
#         self.children = {}  # 存储子节点
#         self.count = 0  # 记录该字符被多少个单词访问过

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#             node.count += 1  # 每次插入字符就+1

#     def longest_prefix(self, total_words):
#         node = self.root
#         prefix = ""

#         while node and len(node.children) == 1:  # 只有一个分支
#             char = next(iter(node.children))  # 获取唯一的字符
#             if node.children[char].count == total_words:
#                 prefix += char
#                 node = node.children[char]
#             else:
#                 break  # 出现次数不足，不是公共前缀
        
#         return prefix

# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if not strs:
#             return ""

#         trie = Trie()
#         for word in strs:
#             trie.insert(word)  # 插入Trie

#         return trie.longest_prefix(len(strs))  # 查找最长公共前缀

#Correct Version################################################################
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: #check empty string
            return ""
        prefix = strs[0] #the first element(string) in list
        for string in strs[1:]: #each string in list starting from second
            while string.find(prefix) != 0: #while the "prefix" not found in current string
                prefix = prefix[:-1] # reduce the last digit of "prefix"
                if not prefix: # if the prefix have nothing left
                    return "" #result is nothing
        return prefix #otherwise this is the answer