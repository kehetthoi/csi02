# a=input("nhập họ:")
# b=input("nhập tên lót:")
# c=input("nhập tên:")
# print(a,b,c)


a=int(input("nhap so phan tu :"))
arr=[]
for i in range(a):
    ptu=int(input(f"nhap phan tu thu {i+1}:"))
    arr.append(ptu)
if len(arr) < 2:
    print("ko tim thay")
else:
    solon = sorted(set(arr), reverse=True)
    if len(solon) < 2:
        print("ko tim thay")
    else:
        print("so lon t2 la =", solon[1])


# class HinhChuNhat:
#     def __init__(self, dai, rong):
#         self.dai = dai
#         self.rong = rong

#     def chuvi(self):
#         return 2 * (self.dai + self.rong)

#     def dientich(self):
#         return self.dai * self.rong

# class HinhVuong(HinhChuNhat):
#     def __init__(self, canh):
#         super().__init__(canh, canh)
# a=int(input("nhap cd:"))
# b=int(input("nhap cr:"))
# c=int(input("nhap canh:"))
# hcn= HinhChuNhat(a,b)
# hv = HinhVuong(c)
# print("Chu vi hình chữ nhật:", hcn.chuvi())
# print("Diện tích hình chữ nhật:", hcn.dientich())
# print("Chu vi hình vuông:", hv.chuvi())
# print("Diện tích hình vuông:", hv.dientich())



# a = float(input("nhap so: "))
# if a.is_integer():
#     print(f"{a} là số nguyên")
# else:
#     print(f"{a} không phải sô nguyên")
