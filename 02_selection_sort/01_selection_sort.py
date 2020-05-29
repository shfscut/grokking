# coding:utf8

"""
从小到大排序

1.copy同样大小的数组
2.选择剩余数组中的最小值，追加到新数组中
"""

def get_smallest_index(source_list):
    min=source_list[0]
    index = 0
    for i, val in enumerate(source_list):
        if val < min:
            index = i

    return index


def select_sort(source_list):

    new_source_list=[]

    while source_list:
        index=get_smallest_index(source_list)
        new_source_list.append(source_list[index])
        source_list.pop(index)
    return new_source_list
    


if __name__=='__main__':
    source_list=[2,4,5,6,1,34,3,8]
    new_list = select_sort(source_list)
    print(new_list)
