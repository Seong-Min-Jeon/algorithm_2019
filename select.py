def selection_sort(List):
    
    num = 1
    max = List[0]
    idx = 0

    for j in range(len(List)):
        for i in range(len(List) - num + 1):
            temp = List[i]
            if max <= temp:
                max = temp
                idx = i
        num2 = List[len(List) - num]
        List[len(List) - num] = max
        List[idx] = num2
        num += 1
        max = List[0]
    return List

def selection_sort2(List):
    
    num = 1
    min = List[0]
    idx = 0

    for j in range(len(List)):
        for i in range(len(List) - num + 1):
            temp = List[i]
            if min >= temp:
                min = temp
                idx = i
        num2 = List[len(List) - num]
        List[len(List) - num] = min
        List[idx] = num2
        num += 1
        min = List[0]
    List.reverse()


List = [6,2,1,4,5,3]
List2 = [6,2,1,4,5,3]

selection_sort(List)
selection_sort2(List2)

#print(List)
#print(List2)
