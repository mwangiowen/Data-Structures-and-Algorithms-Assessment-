def is_balanced(expression):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs.keys():
            if not stack or stack.pop() != bracket_pairs[char]:
                return False

    return not stack


expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1)) 
print(is_balanced(expression2))  
