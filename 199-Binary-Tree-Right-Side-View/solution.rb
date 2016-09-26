# @param {TreeNode} root
# @return {Integer[]}
def right_side_view(root)
  return [] if root.nil?
  queue = Queue.new
  queue.push(root)
  res = []
  while (!queue.empty?)
    count = queue.length
    while count > 0
      last = queue.pop()
      count -= 1
      queue.push(last.left) unless last.left.nil?
      queue.push(last.right) unless last.right.nil?
    end
    res.push(last.val)
  end
  res
end
