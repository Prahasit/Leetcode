class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_str = ""
        for i in s:
            if i.isalnum():
                valid_str += i.lower()

        return valid_str == valid_str[:: -1]

