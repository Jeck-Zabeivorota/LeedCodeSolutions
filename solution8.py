class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        '''
        Повертає округленний результат ділення `dividend` на `divisor`. `¯\_(ツ)_/¯`

        Але в ході виконання не використовуються операції ділення, множення або mod (залишок від ділення),
        при тому швидкість виконання висока.
        ```
        divide(5, 2) -> 2
        ```
        '''

        if dividend == 0 or divisor == 0:
            return 0
        
        def invert(num: int) -> int:
            return num - num - num
        
        def getResult(num: int, is_minus: bool) -> int:
            num = invert(num) if is_minus else num
            return 2147483647 if num == 2147483648 else num

        if dividend > 0 and divisor > 0:
            is_minus = False
        elif dividend < 0 and divisor < 0:
            dividend = invert(dividend)
            divisor = invert(divisor)
            is_minus = False
        elif dividend < 0:
            dividend = invert(dividend)
            is_minus = True
        else:
            divisor = invert(divisor)
            is_minus = True

        if dividend == divisor:
            return -1 if is_minus else 1
        
        if dividend == 1 or dividend < divisor:
            return 0
        if divisor == 1:
            return getResult(dividend, is_minus)

        count = 0
        while True:
            multi_divisor = divisor
            quantity = 1
            
            while dividend - multi_divisor >= 0:
                dividend -= multi_divisor
                count += quantity
                multi_divisor += multi_divisor
                quantity += quantity

            if quantity == 1:
                break
        
        return getResult(count, is_minus)
                

s = Solution()
print(s.divide(9, 3))