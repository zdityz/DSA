class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        num = "0123456789"
        chars = []
        for i in s.lower():
            if i in alpha or i in num:
                chars.append(i)
        word = ''.join(chars)
        
        left = 0
        right = len(chars) - 1

        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

        rev = ""
        for ch in chars:
            rev += ch

        if rev==word:
            return True
        else:
            return False