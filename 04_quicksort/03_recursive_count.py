"""

基线条件：当arr=[], 返回len(arr)=0， 当len(arr)==1,返回1
"""

def count(arr):
    if len(arr)==0:
        return 0
    if len(arr)==1:
        return 1
    arr.pop()
    return 1 + count(arr)


if __name__ == '__main__':
    t=count([1,2])
    print(t)