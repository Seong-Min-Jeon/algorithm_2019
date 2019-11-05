def merge_sort(List):
    if(len(List) <= 1):
        return List
    middle = len(List) // 2
    left = List[:middle]
    right = List[middle:]
    re_left = merge_sort(left)
    re_right = merge_sort(right)
    return merge(re_left,re_right)

def merge(left, right):
    left_num = 0
    right_num = 0
    sorted_list = []
    try:
        while(True):
            if (left[left_num] < right[right_num]):
                sorted_list.append(left[left_num])
                left_num += 1
            else:
                sorted_list.append(right[right_num])
                right_num += 1
    except:
        if (len(left) <= left_num):
            final_list = sorted_list + right[right_num:len(right) + 1]
        else:
            final_list = sorted_list + left[left_num:len(left) + 1]
    List = final_list 
    return List

List = [6,2,1,4,5,3]
sorted_list = merge_sort(List)
#print(sorted_list)




