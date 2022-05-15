import copy

EMPTY = 0
PLUS = 1
MINUS = 2
MUL = 3
DIV = 4

TARGET = 100


def calc_empty(signs:list):
    new_vals = []
    new_signs = []
    val = 1
    for i in range(len(signs)):
        add = i+2

        if signs[i] == EMPTY:
            val = val*10+add
        else:
            new_vals.append(val)
            new_signs.append(signs[i])
            val = add
    new_vals.append(val)
    return (new_vals, new_signs)


def calc_mul_div(vals:list, signs:list):
    new_vals = []
    new_signs = []
    val = vals[0]

    for i in range(len(signs)):
        add = vals[i+1]
        if signs[i] == MUL:
            val *= add
        elif signs[i] == DIV:
            val /= add
        else:
            new_vals.append(val)
            new_signs.append(signs[i])
            val = add
    new_vals.append(val)
    return (new_vals, new_signs)


def calc_plus_minus(vals:list, signs:list):
    res = vals[0]
    for i in range(len(signs)):
        add = vals[i+1]
        if signs[i] == PLUS:
            res += add
        elif signs[i] == MINUS:
            res -= add

    return res


def calc(signs:list):
    step1 = calc_empty(signs)
    step2 = calc_mul_div(step1[0], step1[1])
    return calc_plus_minus(step2[0], step2[1])


def decode(sign:list):
    res = "1"
    for i in range(len(sign)):
        if sign[i] == PLUS:
            res += "+"
        elif sign[i] == MINUS:
            res += "-"
        elif sign[i] == MUL:
            res += "*"
        elif sign[i] == DIV:
            res += "/"
        res += str(i+2)
    return res


def rec(vec:list, res:list):
    if len(vec) == 8:
        EPS = 1e-9
        if abs(calc(vec)-TARGET) < EPS:
            res.append(decode(vec))
        return

    for i in range(5):
        vec2 = copy.deepcopy(vec)
        vec2.append(i)
        rec(vec2, res)


if __name__ == "__main__":
    vec = []
    res = []
    rec(vec, res)
    print("The number of solutions:",len(res))
    for r in res:
        print(r,"=",TARGET)
