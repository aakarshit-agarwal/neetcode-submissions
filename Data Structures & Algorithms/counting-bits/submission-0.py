class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
           result.append(self.count1(i)) 
        return result

    def count1(self, n):
        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            n = math.floor(n/2)
        return count