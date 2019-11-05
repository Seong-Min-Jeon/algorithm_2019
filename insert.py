def insertion_sort(List):
    for i in range(len(List) - 1):
        num1 = 0
        num2 = 1
        while(True):
            if (List[i + 1 - num1] < List[i + 1 - num2]):
                temp = List[i + 1 - num1]
                List[i + 1 - num1] = List[i + 1 - num2]
                List[i + 1 - num2] = temp
                if (i + 1 - num2 > 0):
                    num1 += 1
                    num2 += 1
                else:
                    break
            else:
                break
    return List

List = [6,2,1,4,5,3]

insertion_sort(List)

#print(List)