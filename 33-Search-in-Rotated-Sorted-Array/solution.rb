# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def search(nums, target)
  low = 0
  high = nums.length - 1
  while low <= high
    mid = low + (high - low)/2
    return mid if nums[mid] == target
    if(nums[low] <= nums[mid])
      if(nums[low] <= target && target < nums[mid])
        high = mid - 1
      else
        low = mid + 1
      end
    end
    if (nums[mid] <= nums[high])
      if(nums[mid] < target && target <= nums[high])
        low = mid + 1
      else
        high = mid - 1
      end
    end
  end
  return -1
end