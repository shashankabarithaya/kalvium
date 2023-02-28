def longest_valid_parentheses(s):
    stack = [-1]  # Initialize the stack with -1 as the base index.
    max_len = 0  # Initialize the maximum valid substring length to 0.

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:  # s[i] == ')'
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])

    return max_len










# Example usage:
print(longest_valid_parentheses("(()))())("))  # Output: 4
