class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        # Step 1: frequency map of what we NEED (chars in s1)
        seen = {}
        for c in s1:
            seen[c] = seen.get(c, 0) + 1
        
        # How many unique characters we need to fully match
        need = len(seen)
        
        # Step 2: current window frequency
        window = {}
        have = 0          # how many characters currently match their required count
        
        left = 0
        
        # Step 3: slide over s2
        for right in range(len(s2)):
            # Add current character to window
            c = s2[right]
            window[c] = window.get(c, 0) + 1
            
            # If this character is something we care about
            # AND now we have exactly the count we need
            if c in seen and window[c] == seen[c]:
                have += 1
            
            # Step 4: window is too big → shrink from left
            while (right - left + 1) > len(s1):
                remove = s2[left]
                
                # Before removing, check if we are losing a perfect match
                if remove in seen and window[remove] == seen[remove]:
                    have -= 1
                
                # Actually decrease count
                window[remove] -= 1
                if window[remove] == 0:
                    window.pop(remove, None)
                
                left += 1
            
            # Step 5: if we have all required characters with correct counts
            if have == need:
                return True
        
        return False