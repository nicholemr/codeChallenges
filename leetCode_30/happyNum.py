class Solution:
    def isHappy(self, n: int, r: set() = None) -> bool:
        r = r or set()
        squares = []
        for str_num in str(n):
            squares.append(int(str_num)**2)

        sum = 0

        for num in squares:
            sum += num

        if sum == 1:
            return True
        elif sum in r:
            return False
        else:
            r.add(sum)
            return self.isHappy(sum, r)


sol = Solution()
print(sol.isHappy(19))
