import copy


class Sudoku:
    __field = []
    __filepath = ""

    def __init__(self, path) -> None:
        self.__filepath = path

    def input(self):
        with open(self.__filepath) as f:
            for _ in range(9):
                s_line = list(f.readline().rstrip('\n'))
                tmp = []
                for s in s_line:
                    if s != "*":
                        tmp.append(int(s))
                    else:
                        tmp.append(-1)

                self.__field.append(tmp)

    def get(self):
        return self.__field

    def put(self, x: int, y: int, val: int):
        self.__field[x][y] = val

    def reset(self, x: int, y: int):
        self.__field[x][y] = -1

    def find_empty(self) -> bool:
        for x in range(9):
            for y in range(9):
                if self.__field[x][y] == -1:
                    return True, x, y
        return False, x, y

    def find_choices(self, x: int, y: int) -> set:
        """
        マス(x, y)に入る数字の集合を返す

        Parameters
        ---
        x: int
            列の座標
        y: int
            行の座標

        Returns
        ---
        result: set
            マス(x, y)に入る数字の集合
        """

        cannot_use = set()

        #同じ行に含まれる数字を除外
        for i in range(9):
            if self.__field[x][i] != -1:
                cannot_use.add(self.__field[x][i])

        #同じ列に含まれる数字を除外
        for i in range(9):
            if self.__field[i][y] != -1:
                cannot_use.add(self.__field[i][y])

        #同じブロックに含まれる数字を除外
        x2 = x//3*3
        y2 = y//3*3
        for i in range(x2, x2+3):
            for j in range(y2, y2+3):
                if self.__field[i][j] != -1:
                    cannot_use.add(self.__field[i][j])

        result = set(num for num in range(1, 10))
        result -= cannot_use

        return result


def dfs(board: Sudoku, res: list, all: bool = True):

    if not all and len(res) == 0:
        return True

    is_empty, x, y = board.find_empty()
    if not is_empty:
        now_ans=copy.deepcopy(board.get())
        res.append(now_ans)
        return True
    
    can_use = board.find_choices(x, y)
    for val in can_use:
        board.put(x, y, val)
        dfs(board, res, all)
        if not is_empty:
            return True
        else:
            board.reset(x, y)


def solve(board: Sudoku, all: bool = True):
    res = []
    dfs(board, res, all)
    return res


if __name__ == "__main__":
    board = Sudoku("chap2/sec1/input.txt")
    board.input()

    res = solve(board)
    if len(res) == 0:
        print("No Solutions")
    elif len(res) > 1:
        print("More than one solution.")
    else:
        answer = res[0]
        for i in range(9):
            print(" ".join(str(num) for num in answer[i]))
