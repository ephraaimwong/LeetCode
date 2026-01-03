class Solution(object):
   
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        """
        --- Solution Intent 1 (spamming conditionals) ---
        if current token is left bracket, append to stack
        if current token is right bracket and stack peek == corresponding bracket >> pop()
        return true if stack is empty at end
        """    
        
        def peek(stack):
            if stack:
                return stack[-1]
            else:
                return None

        stack = []

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')' and peek(stack) == '(':
                stack.pop()
            elif i == '}' and peek(stack) == '{':
                stack.pop()
            elif i == ']' and peek(stack) == '[':
                stack.pop()
            else:
                return False

            # print(stack)
        return not bool(stack)
    
        """
        --- Solution Intent 2 (using hashmap) ---
        if current token is left bracket, append to stack
        if current token is right bracket, pop from stack(only left brackets) and compare if pop's complement == current token
        return true if stack is empty at end
        """    
        complement = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        
        stack = []

        for i in s:
            if i in complement: # right brackets
                if not stack: #stack empty
                    return False
                elif complement[i] != stack.pop(): #hashmap(rightbrack)=leftbrack, if not equal, immediate failure
                    return False
            elif i in "({[": # left brackets
                stack.append(i)
            # print(stack)
        return not stack