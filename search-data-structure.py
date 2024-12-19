
class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not c in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        
        def search_app(curr, word) -> bool:
            i = 0
            for c in word:
                if c == '.':
                    for child in curr.children.values():
                        if search_app(child, word[i+1:]):
                            return True
                    return False
                else:
                    if c in curr.children:
                        curr = curr.children[c]
                    else:
                        return False
                i += 1
            return curr.isWord

                

        i = 0
        for c in word:
            if c == '.':
                for child in curr.children.values():
                    if search_app(child, word[i+1:]):
                        return True
                return False
            else:
                if c in curr.children:
                    curr = curr.children[c]
                else:
                    return False
            i += 1
        return curr.isWord
            
        
