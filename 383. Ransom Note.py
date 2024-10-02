class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        check = list(magazine)

        for i in ransomNote:
            if i in check:
                check.remove(i)
            else:
                return False

        return True






