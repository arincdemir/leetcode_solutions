from typing import *

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])

        trie = Trie()
        for word in words:
            trie.add(word)
        
        ans = set()

        def dfs(i, j, node, visited, word):
            if i < 0 or j < 0 or i >= n or j >= m or (i, j) in visited or board[i][j] not in node.children:
                return
            
            visited.add((i, j))
            word = word + board[i][j]
            node = node.children[board[i][j]]
            if node.endOfWord:
                ans.add(word)
            
            dfs(i - 1, j, node, visited, word)
            dfs(i + 1, j, node, visited, word)
            dfs(i, j - 1, node, visited, word)
            dfs(i, j + 1, node, visited, word)

            visited.remove((i, j))
        
        for i in range(n):
            for j in range(m):
                dfs(i, j, trie.root, set(), "")
        
        return list(ans)

        
            