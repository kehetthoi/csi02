import time

# Selection Sort
def select(arr):
    comparisons = 0
    for i in range(len(arr)):
        nho = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[nho] > arr[j]:
                nho = j
        arr[i], arr[nho] = arr[nho], arr[i]
    return arr, comparisons

# Bubble Sort
def bubble(arr):
    comparisons = 0
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, comparisons

# Insertion Sort
def insertion(arr):
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr, comparisons

# Hàm chính
def main():
    n = int(input("Nhập số phần tử (1 ≤ n ≤ 50): "))
    if n < 1 or n > 50:
        print("Số phần tử không hợp lệ!")
        return

    print("Nhập các chuỗi (không quá 20 ký tự):")
    arr = [input().strip()[:20] for _ in range(n)]

    for al, func in [("Selection Sort", select),
                     ("Bubble Sort", bubble),
                     ("Insertion Sort", insertion)]:
        print(f"\n{al}:")
        arr_copy = arr.copy()
        start_time = time.time()
        sorted_arr, comparisons = func(arr_copy)
        exec_time = time.time() - start_time
        print("Danh sách sau khi sắp xếp:", sorted_arr)
        print("Số lần so sánh:", comparisons)
        print("Thời gian thực thi:", f"{exec_time:.6f} giây")

if __name__ == "__main__":
    main()


     



            