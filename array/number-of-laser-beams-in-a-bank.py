class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        if len(bank) < 2:
            return 0

        res = 0
        prev = bank[0].count('1')
        for i in range(1, len(bank)):
            laser_count = bank[i].count('1')
            if laser_count == 0:
                continue
            res += laser_count*prev
            prev = laser_count
        return res