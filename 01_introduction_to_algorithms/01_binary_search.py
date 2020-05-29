#coding: utf8

def get_data_by_binary_search(target, source_list):

    min=0
    max=len(source_list)-1

    while min<=max:
        mid=(min+max)//2
        if source_list[mid]==target:
            return mid

        if source_list[mid]>target:
            max=mid-1
        else:
            min=mid+1

if __name__=='__main__':
    source_list=[1,3,5,7,9,10,12,14,15,18]
    res=get_data_by_binary_search(14, source_list)
    print(res)
