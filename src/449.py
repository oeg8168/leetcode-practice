# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        elements = []
        queue = []
        queue.append(root)

        while any(queue):
            temp = queue.pop(0)
            if temp is None:
                elements.append(None)
            else:
                elements.append(temp.val)
                queue.append(temp.left if temp.left else None)
                queue.append(temp.right if temp.right else None)

        return ','.join(map(str, elements))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data is '':
            return []
        ans = [int(e) if e.isdigit() else None for e in data.split(',')]
        return ans
        

# codec = Codec()
# codec.deserialize(codec.serialize(root))