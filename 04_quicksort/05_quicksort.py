"""

基准条件

递归条件
"""

def quicksort(src_list):
    if len(src_list) == 0:
        return []
    if len(src_list) ==1:
        return [src_list[0]]

    pivot=src_list[0]
    left = [val for val in src_list[1:] if val<pivot]
    right = [val for val in src_list[1:] if val > pivot]

    return quicksort(left)+ [pivot] + quicksort(right)


if __name__ == '__main__':
    t=quicksort([8,4,3,2,12,54,9])
    print(t)