class Solution:
    def winnerSquareGame(self, n):

        if n == 1:
            return True

        # Initialize dp list
        arr = [0, 1]
        for i in range(2, n + 1):

            # Calculate max root integer of i
            root = int(i ** 0.5)

            # If i is square number then dp[i] is True
            if root ** 2 == i:
                arr.append(1)
            else:
                # Iterate all square numbers smaller than i, if find one is False, then dp[i] is True
                for j in range(1, root + 1):
                    if not arr[i - j ** 2]:
                        arr.append(1)
                        break

            # If there's nothing find, dp[i] is False
            if len(arr) == i:
                arr.append(0)

        if arr[n] == 1:
            return True
        else:
            return False
ans = Solution()
n = 7
print(ans.winnerSquareGame(n))

print(4**2)