# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Integer[]}
def inorder_traversal(root)
  return inorder(root)
end

def inorder(root)
  return [] if root.nil?
  res = []
  res += (inorder(root.left)) if !root.left.nil?
  res.push(root.val)
  res += (inorder(root.right)) if !root.right.nil?
  res
end