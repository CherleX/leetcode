class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        level = [root] if root else []
        while level:
			depth += 1
			queue = []
			for lev in level:
				if lev.left:
					queue.append(lev.left)
				if lev.right:
					queue.append(lev.right)
			level = queue
        return depth