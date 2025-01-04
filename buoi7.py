#quick sort
list=[]
a=int(input("nhap so phan tu:"))
for i in range(a):
 ptu=int(input(f"ptu tu thu {i+1} la:"))
 list.append(ptu)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
print(quick_sort(list))


#counting sort
list=[]
a=int(input("nhap so phan tu:"))
for i in range(a):
 ptu=int(input(f"ptu tu thu {i+1} la:"))
 list.append(ptu)
def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    return [i for i in range(len(count)) for _ in range(count[i])]
print(counting_sort(list))