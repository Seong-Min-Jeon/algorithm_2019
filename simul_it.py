import argparse
import copy
import random
import timeit
import sys

from bubble import bubble_sort
from insert import insertion_sort
from select import selection_sort
from quick import quick_sort
from merge import merge_sort
from heap import heap_sort
from python_sort import python_sort


def generate(n, method):
    if method == "ASC":
        return list(range(n))
    elif method == "DESC":
        return list(range(n, 0, -1))
    else:
        return random.sample(range(n), n)


if __name__ == '__main__':
    tmp = 0
    for i in range(17):
        print(tmp)
        tmp += 1
        sys.setrecursionlimit(100000)   # Quick sort에서 재귀가 너무 많이 일어날 경우에 대한 대비

        # 명령행 인수를 받아서 처리할 수 있도록
        parser = argparse.ArgumentParser("Benchmark for sort algorithms")
        parser.add_argument("n", type=int, help="number of data")
        parser.add_argument('-m', default='RANDOM',
                            choices=['ASC', 'DESC', 'RANDOM'], help="method for data generation")
        args = parser.parse_args()
        print(args)
        data = generate(args.n, args.m)
        if len(data) < 30:
            print("Data: ", data)
        algorithms = [insertion_sort, selection_sort, bubble_sort,
                    quick_sort, merge_sort, heap_sort, python_sort]           
        for sort in algorithms:
            if len(data) > 10000 and sort.__name__ in ('insertion_sort', 'selection_sort', 'bubble_sort'):
                continue
            d = copy.deepcopy(data)
            print(sort.__name__, end=":\t")
            print("%.3f" %
                timeit.timeit(
                    'sort(d)', 'from __main__ import sort, d', number=1))

            with open ("data.txt", "a") as f:
                f.write("%.3f" %
                    timeit.timeit(
                        'sort(d)', 'from __main__ import sort, d', number=1))
                f.write(" ")
                
            if len(d) < 30:
                print(d)

            if sorted(data) != d:
                print("something wrong")

    with open('data.txt', 'r') as f:
        data = f.read().replace('\n', '')
    list_data = data.split()
    
    sum_insert = 0
    sum_select = 0
    sum_bubble = 0
    sum_quick = 0
    sum_merge = 0
    sum_heap = 0
    sum_python = 0

    for j in range(10):
        sum_insert += float(list_data[7*j])
        sum_select += float(list_data[1 + 7*j])
        sum_bubble += float(list_data[2 + 7*j])
        sum_quick += float(list_data[3 + 7*j])
        sum_merge += float(list_data[4 + 7*j])
        sum_heap += float(list_data[5 + 7*j])
        sum_python += float(list_data[6 + 7*j])
    
    avg_insert = sum_insert / 10
    avg_select = sum_select / 10
    avg_bubble = sum_bubble / 10
    avg_quick = sum_quick / 10
    avg_merge = sum_merge / 10
    avg_heap = sum_heap / 10
    avg_python = sum_python / 10

    print(avg_insert," ",avg_select," ",avg_bubble," ",avg_quick," ",avg_merge," ",avg_heap," ",avg_python)