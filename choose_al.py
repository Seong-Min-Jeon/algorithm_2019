def sort(List):
    
    num = 1
    max = 0
    idx = 0

    for j in range(len(List)):
        for i in range(len(List) - num + 1):
            temp = List[i]
            if max < temp:
                max = temp
                idx = i
        num2 = List[len(List) - num]
        List[len(List) - num] = max
        List[idx] = num2
        num += 1
        max = 0

List = [6,2,1,4,5,3]

sort(List)

print(List)
