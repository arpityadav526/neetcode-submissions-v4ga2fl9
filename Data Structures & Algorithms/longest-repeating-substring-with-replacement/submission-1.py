class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       
        count = {}
        
        left = 0
      
        max_freq = 0
        
        max_length = 0

 
        for right in range(len(s)):
            
            count[s[right]] = count.get(s[right], 0) + 1
           
            max_freq = max(max_freq, count[s[right]])

            # Check if the current window is invalid (requires more than k replacements)
            # A window is invalid if window size - max_freq > k
            if (right - left + 1) - max_freq > k:
                # Shrink the window from the left by moving the left pointer
                count[s[left]] -= 1
                left += 1
            
           
            max_length = max(max_length, right - left + 1)

        return max_length

