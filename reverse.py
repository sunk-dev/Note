import math as m
try_num=int(input())
final_result=0
def return_result_depend_operator(n1,operator,n2):
    result=0
    n1=int(n1)
    n2=int(n2)
    if operator=='+':
        result=n1+n2
    elif operator=='-':
        result=n1-n2
    elif operator=='-':
        result=n1*n2
    else:
        result=m.trunc(n1/n2)
    return result
    

for i in range(try_num):
    n1,operator,n2=map(str,input().split(' '))
    final_result+=return_result_depend_operator(n1,operator,n2)

print(final_result)