class PrefixTree:

    def __init__(self):
        self.prefix_tree = {}

    def insert(self, word: str) -> None:
        current_tree_node = self.prefix_tree
        for char in word:
            if char not in current_tree_node.keys():
                current_tree_node[char] = {}
            current_tree_node = current_tree_node[char]
        current_tree_node["EOW"] = True

    def search(self, word: str) -> bool:
        current_tree_node = self.prefix_tree
        for char in word:
            if char not in current_tree_node.keys():
                return False
            current_tree_node = current_tree_node[char]
        return True if "EOW" in current_tree_node.keys() else False
        

    def startsWith(self, prefix: str) -> bool:
        current_tree_node = self.prefix_tree
        for char in prefix:
            if char not in current_tree_node.keys():
                return False
            current_tree_node = current_tree_node[char]
        return True
        
        