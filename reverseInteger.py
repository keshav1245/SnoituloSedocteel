class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0] == '-':
            rev_int = int(str(x)[0] + str(x)[1::][::-1])
        else:
            rev_int = int(str(x)[::-1])
            
        rev_int = int(str(x)[0] + str(x)[1::][::-1])
        if rev_int >= -(2**31) and rev_int <= 2**31 - 1:
            return rev_int
        else:
            return 0
        
