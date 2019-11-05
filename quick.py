def quick_sort(List):
    if len(List) <= 1:
        return List
    pivot = List[0]
    left, center, right = [], [], []
    for num in List:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            center.append(num)
    return quick_sort(left) + center + quick_sort(right)

List = [0,6,2,1,4,5,3]

final_list = quick_sort(List)

#print(final_list)

