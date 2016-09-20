# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Integer}
def min_depth(root)
  return 0 if root.nil?
  return 1 + min_depth(root.left) if root.right.nil?
  return 1 + min_depth(root.right) if root.left.nil?
  return 1 + [min_depth(root.left), min_depth(root.right)].min

end