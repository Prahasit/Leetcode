class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        #determine the sum
        res = []
        if (numerator < 0) != (denominator < 0):
            res.append('-')
        #after sign now work with absolutie values
        num, den = abs(numerator), abs(denominator)

        # interger part
        res.append(str(num//den))
        rem = num % den

        # if no remainder then return
        if rem == 0:
            return "".join(res)

        #if there is remainder 
        res.append('.')
        rem_map = {}

        while rem != 0:
            if rem in rem_map: # i.e cycle is repeating
                pos = rem_map[rem]
                res.insert(pos, '(')
                res.append(')')
                return  "".join(res)

            rem_map[rem] = len(res)
            rem *= 10
            res.append(str(rem // den))
            rem %= den
        return "".join(res)
