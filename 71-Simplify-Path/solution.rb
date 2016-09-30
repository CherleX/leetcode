# @param {String} path
# @return {String}
def simplify_path(path)
  items = path.split('/')
  res = []
  0.upto(items.length - 1) do |index|
    if items[index] == '..'
      res.pop
    elsif items[index] == '.' || items[index] == ''
      next
    else
      res.push(items[index])
    end
  end
  "/#{res.join('/')}"
end