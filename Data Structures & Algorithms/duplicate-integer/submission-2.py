class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        hasSeen = {}

        for num in nums:
            if num in hasSeen:
                return True
            hasSeen[num] = 1
        return False
            
                
        
        
    
        
