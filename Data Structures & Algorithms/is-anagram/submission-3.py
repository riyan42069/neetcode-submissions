class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #I -> two strings O -> bool P->return true if same characters for both words
        if len(s) != len(t):
            return False

        s_dict = {}
        

        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            

        for x in t:
            if x not in s_dict or s_dict[x] == 0:
                return False
            s_dict[x] -= 1
        return True