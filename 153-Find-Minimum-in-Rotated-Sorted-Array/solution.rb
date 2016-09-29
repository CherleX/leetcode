# @param {Integer[]} nums
# @return {Integer}
def find_min(nums)
  low = 0
  high = nums.length-1
  while low < high
    mid = (low+high)/2
    if nums[mid] > nums[high]
      low = mid+1
    else
      high = mid
    end
  end
  nums[low]
end
