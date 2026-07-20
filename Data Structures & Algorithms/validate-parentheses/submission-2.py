class Solution:
    def isValid(self, s: str) -> bool:
        
        hashmap = {')':'(', ']':'[', '}':'{'}
        stack = []

        for ch in s:
            if ch not in hashmap:
                stack.append(ch)  # ( + [ + { 
            else:
                if not stack: #if stack is empty 
                    return False
                else: 
                    popped = stack.pop() #popped stores the popped values from the stack
                    if popped!= hashmap[ch]:  #popped value doesnt match the hashmap key:value
                        return False 
        return not stack

        
            