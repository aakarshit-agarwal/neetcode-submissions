# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        return self.s_dfs(root)
        
    def s_dfs(self, node):
        if node == None:
            return "N"
        return str(node.val) + '#' + self.s_dfs(node.left) + self.s_dfs(node.right)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        root_node, _ = self.d_dfs(data, 0)
        return root_node

    def d_dfs(self, data, index):
        if data[index] == 'N':
            return None, index+1
        value = 0
        while data[index] != '#':
            value = value * 10 + int(data[index])
            index += 1
        node = TreeNode(value)
        node.left, new_index = self.d_dfs(data, index+1)
        node.right, new_index = self.d_dfs(data, new_index)
        return node, new_index

