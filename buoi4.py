#selection sort
# a = int(input("nhap so ptu: "))
# list = []
# for i in range(a):
#     ptu = int(input(f"ptu thu {i + 1} la: "))
#     list.append(ptu)
# def selection(arr):
#     for i in range(len(arr)):
#         nho = i
#         for x in range(i +1, len(arr)):
#             if arr[nho] > arr[x]:
#                 nho = x
#         arr[i], arr[nho] = arr[nho], arr[i]
#         return arr
# selection(list) 
# print("Danh sach sau khi sap xep:", list)


#bubble sort
# a = int(input("nhap so ptu: "))
# list = []
# for i in range(a):
#     ptu = int(input(f"ptu thu {i + 1} la: "))
#     list.append(ptu)
# def bubble(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
# print(bubble(list))



#insertion sort
a = int(input("nhap so ptu: "))
list = []
for i in range(a):
    ptu = int(input(f"ptu thu {i + 1} la: "))
    list.append(ptu)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
print(insertion_sort(list))
