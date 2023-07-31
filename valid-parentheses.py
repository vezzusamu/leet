#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def getOpeningBracket(self, bracket):
        if bracket == ')':
            return '('
        elif bracket == '}':
            return '{'
        elif bracket == ']':
            return '['
        else:
            return None

    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if self.getOpeningBracket(bracket) == None:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                if stack.pop() != self.getOpeningBracket(bracket):
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

def main():
    solution = Solution()
    test_cases = ["(){}[]", "({[]})", "{[}]}", "(())", "())"]
    for test_case in test_cases:
        result = solution.isValid(test_case)
        print(f"Input: {test_case}, Valid: {result}")


if __name__ == "__main__":
    main()



        

