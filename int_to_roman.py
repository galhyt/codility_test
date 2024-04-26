class Solution:
    symbols = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }

    symbols_arr = tuple(sorted(symbols.keys(), reverse=True))

    def int_to_roman(self, num: int, symbols_arr=symbols_arr) -> str:
        if num == 0:
            return ''
        i = 0
        while num < symbols_arr[i]:
            i += 1
        k = symbols_arr[i]
        s = self.symbols[k]
        res = num - k
        rom = s + self.int_to_roman(res)

        return rom

    def intToRoman(self, num: int) -> str:
        return self.int_to_roman(num)


if __name__ == '__main__':
    sol = Solution()
    for num in range(901, 1001):
        rom = sol.intToRoman(num)
        print(f"{num} = {rom}")
