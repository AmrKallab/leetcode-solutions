class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for i in s :
            if i in '([{' :
                stack.append(i)
            else :
                if not stack :
                    return False 
                else :
                    if i == ')' :
                        if stack[-1] == '(' :
                            stack.pop()
                        else :
                            return False
                    elif i ==']' :
                        if stack[-1] == '[' :
                            stack.pop()
                        else :
                            return False
                    
                    elif i == '}' :
                        if stack[-1] == '{' :
                            stack.pop()
                        else :
                            return False
        return stack == []