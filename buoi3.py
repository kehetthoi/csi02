# a=int(input("nhap so ptu:"))
# list=[]
# b=int(input("nhap so muon tim:"))
# for i in range(a):
#     ptu=int(input(f"ptu thu {i+1} la:"))
#     list.append(ptu)
# # if b in list:
# #     print(b)
# # else:
# #     print("khong co ptu trong mang")
# def timso(list,b):
#     for i in list:
#         if b in list:
#             print(b)
#         else:
#             print("ko tim thay ptu")
# print(timso(list,b))


def input_array():
  arr = []
  n = int(input("Nhap so phan tu cua mang: "))
  for i in range(n):
    value = int(input(f"Phan tu thu {i}: "))
    arr.append(value)
  arr.sort()
  return arr
def timkiemnp(arr, b):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == b:
            return mid
        elif arr[mid] < b:
            l = mid + 1
        else:
            r = mid - 1

    return -1
arr=input_array()
b=int(input("nhap gia tri can tim:"))
print(timkiemnp(arr,b))





   
     



  