
nums = [1,2,3]
# nums = [1,2]

def productSelf(nums):
    result = []
    
    if (len(nums)) == 1:
        return nums[:]


    for i in range(len(nums)):
        print("nums->",nums)
        n = nums.pop(0)
        print("n => ",n)
        perms = productSelf(nums)
        print("perms",perms)

        # print(perms)
        # for perm in perms:
        #     if perm:
        #         print("perm",perm)
        
        nums.append(n)

(productSelf(nums))
    
    