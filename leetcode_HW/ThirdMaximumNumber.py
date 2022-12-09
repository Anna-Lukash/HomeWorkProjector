# function return the third distinct maximum number in this array. If the third maximum does not exist, function return the maximum number.
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s_nums = set(nums)
        if len(s_nums) < 3:
            return max(s_nums)
        else:
            max_num = sorted(list(s_nums))
            return max_num[-3]      
        