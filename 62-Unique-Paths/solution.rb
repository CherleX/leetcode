# @param {Integer} m
# @param {Integer} n
# @return {Integer}
def unique_paths(m, n)
  res = Array.new(m) { Array.new(n, 1) }

  1.upto(m-1) do |i|
    1.upto(n-1) do |j|
      res[i][j] = res[i-1][j]+ res[i][j-1]

    end
  end
  res[m-1][n-1]
end