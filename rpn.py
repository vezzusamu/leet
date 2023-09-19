class Solution:
    operators = set({"+","-", "*", "/"})

    def apply_op(self, op: str, el_2:int, el_1:int):
        if op == "/":
            return int(el_1/el_2)
        elif op == "*":
            return int(el_1*el_2)
        elif op == "-":
            return int(el_1 - el_2)
        else:
            return int(el_1 + el_2)
        
    def evalRPN(self, tokens: List[str]) -> int:
        op_stack = []
        for token in tokens:
            if token in self.operators:
                el = self.apply_op(token, op_stack.pop(), op_stack.pop())
                op_stack.append(el)
                continue
            op_stack.append(int(token))
        return op_stack.pop()