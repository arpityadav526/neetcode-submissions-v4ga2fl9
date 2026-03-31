from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        need = Counter(s1)           # what we want
        window = Counter()           # current window state
        
        # First window
        for i in range(len(s1)):
            window[s2[i]] += 1
            
        if window == need:
            return True
        
        # Slide the window
        for i in range(len(s1), len(s2)):
            # Add new character (right side)
            window[s2[i]] += 1
            # Remove old character (left side)
            window[s2[i - len(s1)]] -= 1
            # Clean up if count becomes 0 (optional but good practice)
            if window[s2[i - len(s1)]] == 0:
                del window[s2[i - len(s1)]]
                
            if window == need:
                return True
                
        return False