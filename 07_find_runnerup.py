    n = int(input())
    arr = map(int, input().split())
##use set to find the unique elements in a list.
    res = set(arr)     
    res_list = list(res)
    res_list.sort()
    print(res_list[-2])
