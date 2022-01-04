# 2022.1.2 ��һ�α���

# 2124 ����Ƿ�����A����Bǰ��
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


# 2125 �����еļ���������
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

# 2126 �ݻ�С����
class Solution3:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for a in asteroids:
            if mass < a:
                return False
            mass += a
        return True


