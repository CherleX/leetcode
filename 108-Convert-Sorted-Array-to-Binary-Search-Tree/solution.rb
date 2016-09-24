# @param {Integer[]} nums
# @return {TreeNode}
def sorted_array_to_bst(nums)
  return nil if nums.nil?
  return TreeNode.new(nums[0]) if nums.length < 2
  mid = nums.length / 2
  root = TreeNode.new(nums[mid])
  root.left = sorted_array_to_bst(nums[0..mid - 1]) unless mid - 1>0
  root.right = sorted_array_to_bst(nums[mid+1..nums.length])
  root
end