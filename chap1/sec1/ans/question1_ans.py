import itertools
from tokenize import String
from typing import List


class myStack:
    def __init__(self) -> None:
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)


def calc_poland(exp: String):
    space = myStack()
    for c in exp:
        if c >= "0" and c <= "9":
            add = int(c)
            space.push(add)
        else:
            try:
                second = space.pop()
                first = space.pop()

                if c == "+":
                    space.push(first+second)
                elif c == "-":
                    space.push(first-second)
                elif c == "*":
                    space.push(first*second)
                else:
                    space.push(first/second)
            except ZeroDivisionError:
                pass
    return space.pop()


def decode_poland(exp: String):
    space = myStack()
    for c in exp:
        if c >= "0" and c <= "9":
            add = int(c)
            space.push(add)
        else:
            second = str(space.pop())
            first = str(space.pop())

            if c == "*" or c == "/":
                if len(first) > 1:
                    first = "("+first+")"
                if len(second) > 1:
                    second = "("+second+")"

            if c == "+":
                space.push(first+"+"+second)
            elif c == "-":
                space.push(first+"-"+second)
            elif c == "*":
                space.push(first+"*"+second)
            else:
                space.push(first+"/"+second)
    return space.pop()


def check(exp: String, target: int, res: List):
    EPS = 1e-9
    try:
        if abs(calc_poland(exp)-target) < EPS:
            res.append(decode_poland(exp))
    except TypeError:
        pass

def solve(val, target):
    res = []

    val.sort()
    for v in list(itertools.permutations(val)):
        fours = ""
        for num in v:
            fours += str(num)
        ops = "+-*/"
        for op1 in ops:
            for op2 in ops:
                for op3 in ops:
                    #パターンnnnnooo を作成
                    exp = fours+op1+op2+op3
                    exp_list=list(exp)
                    #パターンnnnnooo を試す
                    check(exp, target, res)
                    exp_list[3],exp_list[4]=exp_list[4],exp_list[3]
                    check("".join(exp_list),target,res)

                    exp_list[4],exp_list[5]=exp_list[5],exp_list[4]
                    check("".join(exp_list),target,res)

                    exp_list[2],exp_list[3]=exp_list[3],exp_list[2]
                    check("".join(exp_list),target,res)

                    exp_list[4],exp_list[5]=exp_list[5],exp_list[4]
                    check("".join(exp_list),target,res)

    return res

if __name__ == "__main__":
    val = []
    target = 0
    for i in range(4):
        print(i+1, "th number: ", end='')
        val.append(int(input()))
    print("target number: ", end='')
    target = int(input())

    res = solve(val, target)
    for exp in res:
        print(exp,"=",target)
