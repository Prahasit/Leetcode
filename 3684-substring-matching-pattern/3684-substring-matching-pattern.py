class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        def manual_search(text: str, sub: str, start: int) -> int:
            """Manually searches for `sub` in `text` starting from `start`."""
            n, m = len(text), len(sub)
            for i in range(start, n - m + 1):  # Iterate over valid start positions
                match = True
                for j in range(m):  # Compare each character
                    if text[i + j] != sub[j]:  # Compare character-by-character
                        match = False
                        break
                if match:
                    return i
            return -1  # Return -1 if not found

        # Split pattern into left and right parts based on '*'
        left_part, right_part = "", ""
        star_index = -1

        # Manually finding '*'
        for i in range(len(p)):
            if p[i] == '*':
                star_index = i
                break

        if star_index != -1:
            left_part = p[:star_index]
            right_part = p[star_index + 1:]

        # Find left_part manually
        left_idx = manual_search(s, left_part, 0)  # Pass `s`, not `string`
        if left_idx == -1:
            return False  # left_part not found

        # Find right_part manually after left_part
        right_idx = manual_search(s, right_part, left_idx + len(left_part))
        return right_idx != -1  # True if both parts found in order