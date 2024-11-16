# tuple = (1, 2, 3)
# tuple[0] = 10

# num = 3
# num += 10
# print(num)

# num1=13
# num2=6.3
# num3=6
# print(num1+num2*num3)
# print(((num1+num2)*num3)/14)

# a={x*x for x in range(10)}
# print(a)

# a=int(input("nhap so a:"))
# def nhan_a():
#     return 2*a
# print(nhan_a())

# a=float(input("nhap ban kinh:"))
# pi = 3.1416
# def chuvi():
#     return 2*a*pi
# def dt():
#     return pi*a**2
# print(chuvi())
# print(dt())

a=int(input("nhap do dai mang:"))
arr=[]
for i in range(a):
    ptu = int(input("nhap phan tu:"))
    arr.append(ptu)
sum = 0
for num in arr:
    if num%2==0 and num>0:
        sum += num
    elif num<0:
        print("nhap so duong")
        break
print(sum)