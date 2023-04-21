class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        if len(nums)==0:
            return 0

        n=len(nums)           
        maxReach=nums[0]
        step=nums[0]
        ans = 1
        flag = False
        for i in range(1,n):
            maxReach=max(maxReach,i+nums[i])
            
            step-=1
            
            if maxReach >= n-1:
                return ans
            
            if step == 0:
                ans += 1
                step=maxReach-i
        return ans