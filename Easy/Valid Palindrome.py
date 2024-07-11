class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newS = ""
        for letter in s:
            if letter.isalnum():
                newS += letter
        
        p1 = 0
        p2 = len(newS) - 1
        while (p1<p2):
            if newS[p1] != newS[p2]:
                return False
            p1+=1
            p2-=1
        return True