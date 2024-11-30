# list = [x for x in range(10)]
# list2=list(range(10))
# list3=list("abcdef")
# list4 = [1,23,5,1,4,2]
# list4.sort(reverse=True)
# print(list4)

# set=set("abcdef")
# set.add("minhx")
# print(set)

# a = int(input("nhap so phan tu mang 1: "))
# arr = []
# for i in range(a):
#     ptu = int(input(f"nhap phan tu thu {i+1}: "))
#     arr.append(ptu)
# b = int(input("nhap so phan tu mang 2: "))
# list2 = []
# for i in range(b):
#     ptu2 = int(input(f"nhap phan tu thu {i+1}: "))
#     list2.append(ptu2)
# ghep = arr + list2
# ghep.sort(reverse=True)
# print(ghep)

# a = int(input("nhap so phan tu mang 1: "))
# arr = []
# for i in range(a):
#     ptu = int(input(f"nhap phan tu thu {i+1}: "))
#     arr.append(ptu)
# solon = sorted(set(arr), reverse=True)
# sonho =sorted(set(arr), reverse=False)
# tbc=sum(arr)/len(arr)
# kq = (solon[0],sonho[0],tbc)
# print(kq)


chuoi = input("nhap chuoi cach nhau bang dau ';' : ")
tu = chuoi.split(';')
tu.reverse()
tu = [word.capitalize() for word in tu]
ket_qua = " ".join(tu)
print("Kết quả:", ket_qua)





