class Solution:
    def maximum69Number(self, num: int) -> int:
        num_arr = list(str(num))
        for i in range(len(num_arr)):
            if num_arr[i] == '6':  # change the first occurrence of 6 to 9, This will give the max number
                num_arr[i] = '9'
                break
        return int(''.join(num_arr))
