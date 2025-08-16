class Solution:
    def isPerfectSquare(self, num: int) -> bool:
       n1=num
       n2=n1**0.5
       if n1**0.5==int(n2):
        return True
       else:
        return False
