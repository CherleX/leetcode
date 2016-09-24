# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Integer[][]}
def level_order_bottom(root)
  return [] if root.nil?
  res = []
  queue = Queue.new
  queue.push(root)
  while !queue.empty?
    n = queue.size
    r = []
    while n > 0
      node = queue.pop
      n = n - 1
      r.push(node.val)
      queue.push(node.left) unless node.left.nil?
      queue.push(node.right) unless node.right.nil?
    end
    res.push(r)
  end
  res.reverse
end
