# /*
# Design a data structure that supports the following two operations:

# void addWord(word)
# bool search(word)

# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
# */

class Node():
    def __init__(self) -> None:
        self.children = {}
        self.end = False
        
class Trie():
    def __init__(self):
        self.root = Node()
    
    def addWord(self, word):
        node = self.root
        for lt in word:
            if lt not in node.children:
                node.children[lt] = Node()
            node = node.children[lt]
        node.end = True
        
    def searchWord(self, word):
        node = self.root
        for lt in word:
            if lt not in node.children:
                return False
        return node.end