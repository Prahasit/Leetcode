class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def solve(log):
            identifier, content = log.split(" ", 1)# splitting only at 1st space
            is_digit = content[0].isdigit()
            # if digit log, maintaining relative orde, if it is letter log sorting based on content and then identifier.
            # writter  0 for letter logs as they come before digit logs
            return (1,) if is_digit else (0, content, identifier)

        return sorted(logs, key = solve)