# 2022.1.2 第一次比赛

# 2124 检查是否所有A都在B前面
class Solution1:
    def checkString(self, s: str) -> bool:
        index = 0
        for i in range(len(s)):
            index = i
            if s[i] == 'b':
                break
        for i in range(index+1, len(s)):
            if s[i] == 'a':
                return False
        return True


# 2125 银行中的激光束数量
class Solution2:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        m, n = len(bank), len(bank[0])
        last_index = -1
        last_count = 0
        for i, line in enumerate(bank):
            if line == '0' * n:
                continue
            else:
                count = line.count('1')
                res += count * last_count
                last_index = i
                last_count = count
        return res

# 2126 摧毁小行星
class Solution3:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for a in asteroids:
            if mass < a:
                return False
            mass += a
        return True


