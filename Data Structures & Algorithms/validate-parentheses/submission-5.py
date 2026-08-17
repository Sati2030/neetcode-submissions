class Solution:
    def isValid(self, s: str) -> bool:
        stack_opening = []
        stack_closing = []

        for st in s:
            match st:
                case '(' | '[' | '{':
                    stack_opening.append(st)
                case ')':
                    if len(stack_opening) == 0 or stack_opening[len(stack_opening)-1] != '(':
                        stack_closing.append(st)
                        continue
                    stack_opening.pop()
                case ']':
                    if len(stack_opening) == 0 or stack_opening[len(stack_opening)-1] != '[':
                        stack_closing.append(st)
                        continue
                    stack_opening.pop()
                case '}':
                    if len(stack_opening) == 0 or stack_opening[len(stack_opening)-1] != '{':
                        stack_closing.append(st)
                        continue
                    stack_opening.pop()

        return False if len(stack_opening) != 0  or len(stack_closing) != 0 else True