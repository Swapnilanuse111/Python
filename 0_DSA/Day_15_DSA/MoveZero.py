nums = [0,1,0,3,12]
slow=0
for fast in range(len(nums)):
    if nums[fast] != 0:
        nums[slow]=nums[fast]
        slow=slow+1
print(nums)

    