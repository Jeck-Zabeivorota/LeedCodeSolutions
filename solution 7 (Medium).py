class Solution7:
    def reverse(self, x: int) -> int:
        '''
        Повертає перевернуте число `x`.
        ```
        reverse(-4587) -> -7854
        ```
        '''

        x_str = str(x)

        if len(x_str) == 1: return x

        x = int(x_str[::-1]) if x > 0 else -int(x_str[:0:-1])
        
        return x if -2147483648 <= x <= 2147483647 else 0

s = Solution7()
print(s.reverse(-123))