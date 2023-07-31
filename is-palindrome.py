class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join([i for i in s if i.isalnum()])

        for i in range(int(len(s)/2)):
            if not s[i] == s[len(s)-i-1]:
                return False
        return True
            