#計算量が多過ぎて動かない
import copy
from collections import deque

MULTIPLIED_NUMBER_LENGTH=0
MULTIPLY_NUMBER_LENGTH=0
PARTIAL_PRODUCT=[]
def isValid(check_number:str,partialProduct:str):
    tmp_ans=list(check_number)
    if len(partialProduct)!=len(tmp_ans):
        return False
    for i in range(len(partialProduct)):
        if partialProduct[i]=="*":
            continue
        elif partialProduct[i]!=str(tmp_ans[i]):
            return False
    return True

def setMultiplyNumber(multiply_number:deque,multiplied_number:list):
    if len(multiply_number)==MULTIPLY_NUMBER_LENGTH:
        print(multiplied_number,multiply_number)
        return
    
    for i in range(10):
        multiply_number2 = copy.deepcopy(multiply_number)
        int_multiplied_number=int("".join(map(str, multiplied_number)))
        partialProduct=PARTIAL_PRODUCT[len(multiply_number2)+2]
        check_number=str(int_multiplied_number*i)
        is_valid=isValid(check_number,partialProduct)
        if is_valid:
            multiply_number2.appendleft(i)
            #print("部分積",check_number,"が",partialProduct,"と合っているかチェックしたら",check_number,"はok")
            setMultiplyNumber(multiply_number2,multiplied_number)


def setMultipliedNumber(multiplied_number:deque):
    if len(multiplied_number)==MULTIPLIED_NUMBER_LENGTH:
        check_number="".join(map(str, multiplied_number))
        partialProduct=PARTIAL_PRODUCT[0]
        is_valid=isValid(check_number,partialProduct)
        if is_valid:
            #print(check_number,"が",partialProduct,"と合っているかチェックしたら",check_number,"はok")
            multiply_number=deque()
            setMultiplyNumber(multiply_number,list(multiplied_number))
        return
    
    for i in range(10):
        multiplied_number2 = copy.deepcopy(multiplied_number)
        multiplied_number2.appendleft(i)
        setMultipliedNumber(multiplied_number2)



    

if __name__=="__main__":
    with open("chap1/sec3/input.txt") as f:
        s_line = f.readline().split()
        MULTIPLIED_NUMBER_LENGTH=int(s_line[0])
        MULTIPLY_NUMBER_LENGTH=int(s_line[1])
        for _ in range(MULTIPLY_NUMBER_LENGTH+2):
            s_line = f.readline().rstrip('\n')
            PARTIAL_PRODUCT.append(s_line)
    multiplied_number=deque()
    setMultipliedNumber(multiplied_number)
