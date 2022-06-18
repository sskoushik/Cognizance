import numpy as np
nums = np.array([10,11,12,13,14])
print("Original array:")
print(nums)
a = 5
new_nums = np.zeros(len(nums) + (len(nums)-1)*(a))
new_nums[::a+1] = nums
print("\nNew array:")
print(new_nums)