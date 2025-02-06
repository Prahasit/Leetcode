class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        # dividing p into two string one before * and one after * and checking whether it exists in s or not
        left, right = p.split('*')
        left_ind = s.find(left)
        #searches for right part only after end of left part
        right_ind = s.find(right, left_ind + len(left))

        if left_ind == -1 or right_ind == -1:
            return False
        else:
            return True

