# User function Template for python3

class Solution:
    def findOrder(self, dict, N, K):
        dic = {c: set() for i in dict for c in i}
        for i in range(N - 1):
            w1, w2 = dict[i], dict[i + 1]
            mins = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:mins] == w2[:mins]:
                break
            for i in range(mins):
                if w1[i] != w2[i]:
                    dic[w1[i]].add(w2[i])
                    break
        res = []
        visit = {}

        def dfs(p):
            if p in visit:
                return visit[p]
            visit[p] = True
            for i in dic[p]:
                if dfs(i):
                    return True
            visit[p] = False
            res.append(p)

        for p in dic:
            if dfs(p):
                break
        res.reverse()
        return res


# {
# Driver Code Starts
# Initial Template for Python 3

class sort_by_order:
    def __init__(self, s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i

    def transform(self, word):
        new_word = ''
        for c in word:
            new_word += chr(ord('a') + self.priority[c])
        return new_word

    def sort_this_list(self, lst):
        lst.sort(key=self.transform)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        n = int(line[0])
        k = int(line[1])

        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob = Solution()
        order = ob.findOrder(alien_dict, n, k)
        s = ""
        for i in range(k):
            s += chr(97 + i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)

            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)

# } Driver Code Ends