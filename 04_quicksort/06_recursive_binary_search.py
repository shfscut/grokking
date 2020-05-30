"""

二分查找

基线条件：
递归条件：
"""


def binary_search(src_list, start: int, end: int, key):
    mid = int((end + start) / 2)
    if src_list[mid] == key:
        return mid
    if start >= end:
        return None
    elif key > src_list[mid]:
        return binary_search(src_list, mid + 1, end, key)
    elif key < src_list[mid]:
        return binary_search(src_list, start, mid - 1, key)
    return None
