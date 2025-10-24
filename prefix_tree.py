class TrieNode:
    def __init__(self):
        self.children = {}
        self.obj = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, obj: object) -> None:
        node = self.root
        for c in word:
            if c not in node.children: node.children[c] = TrieNode()
            node = node.children[c]
        node.obj = obj

    def search_with_fallback(self, word: str) -> object | None:
        node = self.root
        for c in word:
            if c not in node.children: raise ValueError(f"{word} not found in Trie")
            node = node.children[c]

        while not node.obj:
            node = node.children[sorted(node.children.keys())[0]]
        return node.obj