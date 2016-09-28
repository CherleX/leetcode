# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Boolean}
def valid(root, minNode, maxNode)
  return true if root.nil?
  if((!minNode.nil? && root.val <= minNode.val) || (!maxNode.nil? && root.val >= maxNode.val))
    return false
  end
  valid(root.left,minNode,root) && valid(root.right,root,maxNode)
end

def is_valid_bst(root)
  valid(root, nil, nil)
end