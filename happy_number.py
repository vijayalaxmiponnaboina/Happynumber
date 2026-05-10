class Solution:
    def isHappy(self, n: int) -> bool:
        visited=set()
        while n!=1:
            if n in visited:
                return False
            visited.add(n)
            s=0
            while n>0:
                digit=n%10
                s=s+digit*digit
                n=n//10
            n=s
        return True
            