import copy


def createOps(ops_list):
    if len(ops_list) == 8:
        formula, ans = question2(ops_list)
        if ans == 100 or ans == 100.0:
            print(formula, "=", ans)

        return True

    for i in range(5):
        new_ops_list = copy.deepcopy(ops_list)
        new_ops_list.append(i)
        createOps(new_ops_list)


def question2(ops):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    formula_num = []
    formula_num.append(str(num[0]))
    formula = ""

    for i in range(len(ops)):
        if ops[i] == 0:
            tmp = str(formula_num[-1])
            tmp += str(num[i+1])
            formula_num[-1] = tmp
        else:
            formula_num.append(str(num[i+1]))

    formula = formula_num[0]
    num_id = 1
    for i in range(len(ops)):
        if ops[i] == 0:
            pass
        elif ops[i] == 1:
            formula = formula+"+"+str(formula_num[num_id])
            num_id += 1
        elif ops[i] == 2:
            formula = formula+"-"+str(formula_num[num_id])
            num_id += 1
        elif ops[i] == 3:
            formula = formula+"*"+str(formula_num[num_id])
            num_id += 1
        elif ops[i] == 4:
            formula = formula+"/"+str(formula_num[num_id])
            num_id += 1
    nums_after_calc1 = []
    nums_after_calc1.append(int(formula_num[0]))
    num1 = nums_after_calc1[-1]
    num_id = 1
    for i in range(len(ops)):
        try:
            num2 = int(formula_num[num_id])
        except:
            break
        if ops[i] == 0:
            pass
        elif ops[i] == 3:
            new_num = num1*num2
            nums_after_calc1[-1] = new_num
            num1 = new_num
            num_id += 1
        elif ops[i] == 4:
            new_num = num1/num2
            nums_after_calc1[-1] = new_num
            num1 = new_num
            num_id += 1
        else:
            nums_after_calc1.append(num2)
            num1 = num2
            num_id += 1

    nums_after_calc2 = []
    nums_after_calc2.append(nums_after_calc1[0])
    num1 = nums_after_calc2[-1]
    num_id = 1
    for i in range(len(ops)):
        try:
            num2 = nums_after_calc1[num_id]
        except:
            break
        if ops[i] == 0:
            pass
        elif ops[i] == 1:
            new_num = num1+num2
            nums_after_calc2[-1] = new_num
            num1 = new_num
            num_id += 1
        elif ops[i] == 2:
            new_num = num1-num2
            nums_after_calc2[-1] = new_num
            num1 = new_num
            num_id += 1

    return formula, nums_after_calc2[0]


if __name__ == "__main__":
    ops_list = []
    createOps(ops_list)
