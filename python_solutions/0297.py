from typing import *

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        ans = []

        def maxId(node: Optional[TreeNode], id):
            serial = [str(id), str(node.val)]
            if node.left:
                serial.append(str(id + 1))
                id = maxId(node.left, id + 1)
            else:
                serial.append("n")

            if node.right:
                serial.append(str(id + 1))
                id = maxId(node.right, id + 1)
            else:
                serial.append("n")

            ans.append(",".join(serial))
            return id
        
        maxId(root, 1)
        ans = ":".join(ans)
        return ans
        


        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None
        
        nodes = {}
        splitted = data.split(":")
        # create the nodes and put them in the hashmap with key being their id's
        for msg in splitted:
            values = msg.split(",")
            id = int(values[0])
            node = TreeNode(int(values[1]))
            nodes[id] = node

        possibleRoots = set(nodes.keys())
        for msg in splitted:
            values = msg.split(",")
            rootId = int(values[0])
            rootNode = nodes[rootId]
            if values[2] != "n":
                rootNode.left = nodes[int(values[2])]
                possibleRoots.remove(int(values[2]))
            if values[3] != "n":
                rootNode.right = nodes[int(values[3])]
                possibleRoots.remove(int(values[3]))

        return nodes[list(possibleRoots)[0]]



            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))