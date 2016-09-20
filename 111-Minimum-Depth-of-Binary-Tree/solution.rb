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
  queue = Queue.new
  queue.push(root)
  i = 0
  while !queue.empty?
    i += 1
    count = queue.size
    count.times do
      front = queue.pop
      queue.push(front.left) unless front.left.nil?
      queue.push(front.right) unless front.right.nil?
      if front.left.nil? && front.right.nil?
        return i
      end
    end
  end
  return -1

end