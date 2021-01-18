def binSearch(x, nums):
  if len(nums) == 0:
    return -1
  
  mp = len(nums)//2
  item = nums[mp]
  if item == x:
    return mp
  elif x < item:
    return binSearch(x, nums[:mp])
  
  elif item < x:
    location = binSearch(x, nums[mp+1:])
    if location == -1:
      return location
    else:
      location = location + mp + 1
      return location


print(binSearch(10, [2,3,4,10,40]))