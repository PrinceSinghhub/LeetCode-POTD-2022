class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) == len(t):

            s = sorted(s)
            t = sorted(t)

            s = ''.join(s)
            t = ''.join(t)

            return s == t

            # another approch

        #             check = list(t)

        #             for i in s:
        #                 if i in check:
        #                     check.remove(i)
        #                     continue
        #                 else:
        #                     return False

        #             return True

        else:
            return False

