def rotate_left3(nums):
  temp=nums[0]
  nums[0]=nums[1]
  nums[1]=temp
  tempp=nums[1]
  nums[1]=nums[2]
  nums[2]=tempp
  return nums
  
