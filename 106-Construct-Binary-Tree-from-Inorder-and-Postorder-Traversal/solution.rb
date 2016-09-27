# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {Integer[]} inorder
# @param {Integer[]} postorder
# @return {TreeNode}
def build_tree(inorder, postorder)
  build(inorder, postorder, 0, 0, inorder.length)
end

def build(inorder, postorder, istart, pstart, size)
  return nil if size == 0
  root = TreeNode.new(postorder[pstart + size - 1])
  cur_index = inorder.find_index(root.val)
  lsize = cur_index - istart
  rsize = size - lsize - 1
  root.left = build(inorder, postorder, istart, pstart, lsize)
  root.right = build(inorder, postorder, cur_index + 1, pstart + lsize, rsize)
  root
end