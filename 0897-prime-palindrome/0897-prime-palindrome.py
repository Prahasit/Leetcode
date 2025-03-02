class Solution:
    def primePalindrome(self, n: int) -> int:
        def prime(n):
            if n <= 1:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        def palindrome(n):
            original, reversed_num = n, 0
            while n > 0:
                reversed_num = reversed_num * 10 + n % 10  
                n //= 10  

            return original == reversed_num
        
        if 8 <= n <= 11:  # Special case where 11 is the smallest prime palindrome >= 8
            return 11
        
        i = n
        while True:
            if prime(i) and palindrome(i):
                return i
            i += 1

            if i > 10 and len(str(i)) % 2 == 0:  # Skip even-length numbers
                i = 10 ** len(str(i))  # Jump to the next length category