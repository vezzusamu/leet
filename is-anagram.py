class Solution:
    #O(n log n) solution Time, O(n) space 
    #n is the length of the longest string
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        return sorted(t) == sorted(s)
    
    def isAnagramTimeEfficientSolution(self, s: str, t: str) -> bool:
            a = len(s)
            if a != len(t):
                return False

            #Creates an array representing the 26 letters of the alphabet
            chars = [0] * 26

            #ord() returns the unicode of the character
            for i in range(a):
                chars[ord(s[i]) - ord('a')] += 1
                chars[ord(t[i]) - ord('a')] -= 1

            for i in range(26):
                if chars[i]!=0:
                    return False

            return True