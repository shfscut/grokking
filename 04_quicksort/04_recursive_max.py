"""

基线条件：
当arr=[], 则return None
当arr长度为1， 则返回值为arr[0]
当长度为2,

递归条件：
取出第一个元素跟其他的对比
"""


def _max(attr):
    if len(attr) == 0:
        return None
    if len(attr) == 1:
        return attr[0]

    rest = _max(attr[1:])
    return attr[0] if attr[0] > rest else rest

if __name__ == '__main__':
    t=_max([1,2,3,4,5,6,7,2,8])
    print(t)
