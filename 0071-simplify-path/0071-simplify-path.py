class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        components = path.split("/")

        for files in components:
            if files == "" or files == ".":
                continue
            if files == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(files)

        return "/" + "/".join(stack)
