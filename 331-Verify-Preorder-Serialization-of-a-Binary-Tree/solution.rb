# @param {String} preorder
# @return {Boolean}
def is_valid_serialization(preorder)
  nodes = preorder.split(',')
  slot = 1
  nodes.each { |node|
    return false if slot == 0
    if node == '#'
      slot -= 1
    else
      slot += 1
    end
  }
  slot == 0
end