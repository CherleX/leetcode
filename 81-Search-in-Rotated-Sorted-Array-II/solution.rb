# @param {Integer[]} nums
# @param {Integer} target
# @return {Boolean}
def search(nums, target)
  low= 0
  high = nums.length - 1
  while low <= high
    mid = low + (high - low)/2
    return true if nums[mid] == target
    if (nums[low] < nums[mid])
      if (nums[low] <= target && target < nums[mid])
        high = mid - 1
      else
        low = mid + 1
      end
    elsif nums[low] > nums[mid]
      if (nums[mid] < target && target <= nums[high])
        low = mid + 1
      else
        high = mid - 1
      end
    else
      low += 1
    end

  end
  return false

end