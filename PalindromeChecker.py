class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        divisor = 1
        while x / divisor >= 10:
            divisor *= 10
        
        while x != 0:
            leadingDigit = x // divisor
            trailingDigit = x % 10
            
            if leadingDigit != trailingDigit:
                return False
            
            x = (x % divisor) // 10
            
            divisor = divisor // 100
        return True
