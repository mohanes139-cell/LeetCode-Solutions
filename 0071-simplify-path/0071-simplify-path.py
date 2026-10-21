class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        tokens = path.split("/")
        
        for token in tokens:
            if token == "" or token == ".":
                continue
            elif token == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(token)
                
        return "/" + "/".join(stack)