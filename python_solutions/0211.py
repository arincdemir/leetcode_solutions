class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()   

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.endOfWord = True

    def search(self, word: str, cur = None) -> bool:
        if word == "":
            return cur.endOfWord

        if cur == None:
            cur = self.root

        for i in range(len(word)):
            c = word[i]
            if c == ".":
                for characterNode in cur.children.values():
                    if self.search(word[i + 1:], characterNode):
                        return True
                return False
            elif c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.endOfWord


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)