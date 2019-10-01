def sort(List):
    
    for i in range(len(List) - 1):
        num = 0
        while(i - num >= 0):
            print(List[i + 1],List[i - num])
            print(List)
            if List[i + 1] < List[i - num]:
                temp = List[i + 1]
                List[i + 1] = List[i - num]
                List[i - num] = temp
                i -= 1
            num += 1

List = [6,2,1,4,5,3]

sort(List)

#print(List)