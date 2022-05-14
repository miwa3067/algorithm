import itertools


class myStack:
    def __init__(self) -> None:
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)


def question1(formula):
    calc_stack = myStack()
    for op in formula:
        if op != "+" and op != "-" and op != "*" and op != "/":
            calc_stack.push(op)
        else:
            try:
                second = calc_stack.pop()
                first = calc_stack.pop()
                if op == "+":
                    calc_stack.push(int(first)+int(second))
                elif op == "-":
                    calc_stack.push(int(first)-int(second))
                elif op == "*":
                    calc_stack.push(int(first)*int(second))
                else:
                    calc_stack.push(int(first)/int(second))
            except ZeroDivisionError:
                pass
    ans=calc_stack.pop()
    if ans==10 or ans==10.0:
        return formula


def createFormula(numbers):
    ops = ["+", "-", "*", "/"]
    pattern=["nnnnooo","nnonnoo","nnnonoo","nnonono","nnnoono"]
    numbers_list = list(itertools.permutations(numbers, 4))
    ops_list=list(itertools.permutations(ops,3))
    for ptn in pattern:
        for number_pattern in numbers_list:
            for ops_pattern in ops_list:
                formula=""
                num_idx=0
                ops_idx=0
                for p in ptn:
                    if p=="n":
                        formula+=str(number_pattern[num_idx])
                        num_idx+=1
                    else:
                        formula+=ops_pattern[ops_idx]
                        ops_idx+=1
                return question1(formula)


if __name__ == "__main__":
    createFormula([1, 2, 3, 4])
