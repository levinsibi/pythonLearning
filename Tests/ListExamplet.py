def list_sort(list, order):
    if order == 'A':
        return sorted(list)
    elif order == 'D':
        # list.sort(reverse=True)// will sort original list
        return sorted(list, reverse=True)


l1 = ['apple', 'anar', 'cashew', 'beetroot']
print(len(l1))
for i in range (len(l1)) :
    print(l1[i])
res = list_sort(l1, 'A')
print(res)

res = list_sort(l1, 'D')
print(res)
