# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Void} Do not return anything, modify root in-place instead.
def flattern_node(root, prev)
  return prev if root.nil?
  prev = flattern_node(root.right, prev)
  prev = flattern_node(root.left, prev)
  root.right = prev
  root.left = nil
  prev = root
  return prev
end

def flatten(root)
  flattern_node(root, nil)
end
