# @param {Integer} n
# @return {Integer}
def num_trees(n)
  dp = Array.new(n+1)
  dp[0] = dp[1] = 1

  2.upto(n) do |i|
    dp[i] = 0
    1.upto(i) do |j|
      dp[i] += dp[j-1] * dp[i-j]
    end
  end
  dp[n]
end