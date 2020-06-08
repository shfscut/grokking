# coding: utf8

"""

基准条件：当len(arr)=0 返回0； 当len(arr)=1, 返回arr[0]
"""

def sum(arr):

    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    return arr.pop() + sum(arr)

if __name__ == '__main__':
    t=sum([1,2,3,4,5,6,7])
    print(t)