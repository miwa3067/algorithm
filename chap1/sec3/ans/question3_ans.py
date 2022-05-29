from tokenize import Number


class Mushikui:
    __multi_plicand = ""
    __multi_plier = ""
    __product = ""
    __middle = []
    __res = {}

    def __init__(self, multi_plicand: str, multi_plier: str, product: str, middle: list) -> None:
        self.__multi_plicand = multi_plicand
        self.__multi_plier = multi_plier
        self.__product = product
        self.__middle = middle

    def rec_plier(self, plicand, vec: list) -> None:
        if len(vec) == len(self.__multi_plier):
            plier = decode(vec)

            if not is_valid(plicand*plier, self.__product):
                return

            self.__res[plicand] = plier
            return

        for add in range(1, 10):
            if not is_valid_sub(add, len(vec), self.__multi_plier):
                continue

            if not is_valid(plicand*add, self.__middle[len(vec)]):
                continue

            vec.append(add)
            self.rec_plier(plicand, vec)
            vec.pop()

    def rec_plicand(self, vec: list) -> None:
        if len(vec) == len(self.__multi_plicand):
            vec2 = []
            self.rec_plier(decode(vec), vec2)
            return

        for add in range(10):
            if len(vec) == 0 and add == 0:
                continue
            if not is_valid_sub(add, len(vec), self.__multi_plicand):
                continue

            vec.append(add)
            self.rec_plicand(vec)
            vec.pop()

    def solve(self) -> dict:
        # self.__res[:] = []

        vec = []
        self.rec_plicand(vec)
        return self.__res


def decode(vec: list) -> int:
    res = 0
    order = 1
    for v in vec:
        res += order*v
        order *= 10
    return res


def is_valid(val: int, st: str) -> bool:
    s_val = str(val)
    if len(s_val) != len(st):
        return False
    for i in range(len(s_val)):
        if st[i] == "*":
            continue
        if s_val[i] != st[i]:
            return False
    return True


def is_valid_sub(v: int, k: int, st: str) -> bool:
    c = st[len(st)-1-k]
    if c == "*":
        return True
    real_val = int(c)
    return v == real_val


if __name__ == "__main__":
    with open("chap1/sec3/input_test.txt") as f:
        s_line = f.readline().split()
        MULTIPLIED_NUMBER_LENGTH = int(s_line[0])
        MULTIPLY_NUMBER_LENGTH = int(s_line[1])
        MULTIPLIED_NUMBER = f.readline().rstrip('\n')
        MULTIPLY_NUMBER = f.readline().rstrip('\n')
        MIDDLE = []
        for _ in range(MULTIPLY_NUMBER_LENGTH):
            s_line = f.readline().rstrip('\n')
            MIDDLE.append(s_line)
        SEKI = f.readline().rstrip('\n')
    mushikui = Mushikui(MULTIPLIED_NUMBER, MULTIPLY_NUMBER, SEKI, MIDDLE)
    res = mushikui.solve()

    print("The num of solution:",len(res))
    for k,v in res.items():
        print("solution:",k,"*",v,"=",k*v)
