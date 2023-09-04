k = 0
nums = [0,0,1,1,1,2,2,3,3,4]
i = 0

hash_map = {}
while i < len(nums):
    if nums[i] not in hash_map:
        k += 1
        hash_map[nums[i]] = 1
    else:
        # hash_map[nums[i]] += 1
        print(nums[i])
        print("duplicate value",nums[i])
        nums.pop(i)
    
    i += 1
        
print(k)
print(nums)
print(hash_map)
    