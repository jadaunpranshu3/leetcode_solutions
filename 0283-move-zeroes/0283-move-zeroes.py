class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        for  i in range(n-1):
            for  j in range(i+1,n):
                if nums[i]==0 and nums[j] != 0:
                   nums[i],nums[j]=nums[j],nums[i]
                   break