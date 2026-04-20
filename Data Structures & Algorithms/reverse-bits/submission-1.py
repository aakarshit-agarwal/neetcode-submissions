class Solution:
    def reverseBits(self, n: int) -> int:
        n_str = self.getBinary(n)[::-1]
        print(n_str)
        result = 0
        for i in range(32):
            if n_str[i] == '1':
                result += 2 ** (31-i)
        return result

    def getBinary(self, n):
        binary = ''
        while n > 0:
            if n % 2 == 1:
                binary = '1' + binary
            else:
                binary = '0' + binary
            n = math.floor(n/2)
        binary = '0'*(32-len(binary)) + binary 
        return binary