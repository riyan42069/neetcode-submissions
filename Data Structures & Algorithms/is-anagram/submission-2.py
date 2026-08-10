class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #I -> two strings O -> bool P->return true if same characters for both words
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1
        
        print(s_dict)
        print(t_dict)

        if s_dict == t_dict:
            return True
        else:
            return False
