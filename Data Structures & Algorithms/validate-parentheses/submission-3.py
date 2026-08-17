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

        if len(stack_closing) > 0:
            if len(stack_closing) != len(stack_opening):
                return False
            for i in reversed(range(len(stack_closing))):
                if stack_closing[i]  == stack_opening[i]:
                    stack_closing.pop()
                    stack_opening.pop()
                else:
                    return False

        return False if len(stack_opening) != 0 else True