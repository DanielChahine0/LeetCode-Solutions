class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)!=len(t):
        #     return False
        
        # dictS = dict()
        # dictT = dict()
        # for letter in s:
        #     if letter in dictS:
        #         dictS[letter] += 1
        #     else:
        #         dictS[letter] = 1
        # for letter in t:
        #     if letter in dictT:
        #         dictT[letter] += 1
        #     else:
        #         dictT[letter] = 1
        # for key in dictT:
        #     if (key not in dictS) or (dictT[key]!=dictS[key]):
        #         return False
            
        # return True
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        return s == t