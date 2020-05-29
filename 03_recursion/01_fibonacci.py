# coding: utf8

"""

fibonacci数列
F(0)=0
F(1)=1
F(n)=F(n-1)+F(n-2)（n≧2）

递归：
1. 基线条件: 当n=0或1时，不再递归，返回具体值
2. 递归条件: 当n>=2时，递归
"""

def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

if __name__ == '__main__':
    for i in range(10):
        print(fibonacci(i))
    # f(3)+f(2)
    # f(2)+f(1)+f(2)
    # f(1)+f(0)+f(1)+f(1)+f(0)