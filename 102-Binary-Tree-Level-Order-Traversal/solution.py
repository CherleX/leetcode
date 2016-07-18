class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.levelHelper(result, root, 0)
        return result
        
    def levelHelper(self,result,root,level):
        if root is None:
            return
        if len(result)<=level:
            result.append([])
        result[level].append(root.val)
        self.levelHelper(result, root.left, level+1)
        self.levelHelper(result, root.right, level+1)
        
        