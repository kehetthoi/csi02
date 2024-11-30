def input_array():
    arr = []
    n = int(input("Nhập số phần tử của mảng: "))
    for i in range(n):
        value = int(input(f"Phần tử thứ {i}: "))
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

# Nhập mảng và giá trị cần tìm
arr = input_array()
b = int(input("Nhập giá trị cần tìm: "))

# Tìm kiếm và in kết quả
ket_qua = timkiemnp(arr, b)
if ket_qua != -1:
    print(f"Giá trị {b} được tìm thấy tại vị trí {ket_qua}.")
else:
    print(f"Giá trị {b} không tồn tại trong mảng.")

