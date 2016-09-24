# @param {TreeNode} root
# @return {String[]}
def binary_tree_paths(root)
  return [] if root.nil?
  return [root.val.to_s] if root.left.nil? && root.right.nil?
  res = []
  binary_tree_paths(root.left).each { |r| res.push(root.val.to_s + '->'+r) }
  binary_tree_paths(root.right).each { |r| res.push(root.val.to_s + '->'+r) }
  res
end