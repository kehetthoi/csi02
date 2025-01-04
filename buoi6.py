# list=[]
# a=int(input("nhap so phan tu:"))
# for i in range(a):
#  ptu=int(input(f"ptu tu thu {i+1} la:"))
#  list.append(ptu)
# x=int(input("nhap so can tim:"))
# def linear_search(arr,b):
#   for i in range(len(arr)):
#         if arr[i] == b:
#             return i
#   return -1
# print(linear_search(list,x))


# list=[]
# a=int(input("nhap so phan tu:"))
# for i in range(a):
#  ptu=int(input(f"ptu tu thu {i+1} la:"))
#  list.append(ptu)
# def dem(arr):
#  count={}
#  for i in arr:
#   if i in count:
#    count[i] += 1
#   else:
#    count[i] = 1
#  return count
# print(dem(list))  


list=[]
a=int(input("nhap so phan tu:"))
for i in range(a):
 ptu=int(input(f"ptu tu thu {i+1} la:"))
 list.append(ptu)
x=int(input("nhap so can tim:"))
def find_all_positions(arr, b):
    positions = [] 
    for i in range(len(arr)):
        if arr[i] == b:
            positions.append(i + 1)  
    return positions
print(find_all_positions(list,x))

  
 