# 1.biến global là biến được khai báo bên ngoài hàm và có thể sử dụng trong hàm còn biến local là biến được khai báo trong hàm và chỉ có thể sử dụng trong hàm đó
#2.
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#        if n % i == 0:
#             return False
#     return True
# a = int(input("Nhập số: "))
# if is_prime(a):
#     print(f"{a} là số nguyên tố")
# else:
#     print(f"{a} không phải là số nguyên tố") 
#3.
# 1. Trình duyệt (client) gửi một yêu cầu HTTP (HTTP request) đến máy chủ (server) thông qua địa chỉ URL của trang web.
# 2. Máy chủ nhận yêu cầu và xử lý nó. 
# 3. Sau khi xử lý xong, máy chủ gửi lại một phản hồi HTTP (HTTP response) chứa mã HTML của trang web về cho trình duyệt. 
# 4. Trình duyệt nhận phản hồi và hiển thị nội dung trang web cho người dùng. Trình duyệt có thể tiếp tục gửi các yêu cầu bổ sung để tải các tài nguyên khác như hình ảnh, CSS, và JavaScript.
#7.
# INNER JOIN chỉ trả về các hàng có sự khớp trong cả hai bảng.
# LEFT JOIN trả về tất cả các hàng từ bảng bên trái, và các hàng khớp từ bảng bên phải. Nếu không có sự khớp, các cột từ bảng bên phải sẽ chứa giá trị NULL.
#8.
# SELECT customer_id, 
#        SUM(total_amount) AS total_spent
# FROM orders
# GROUP BY customer_id
# HAVING SUM(total_amount) > 10000000;                           
#9.
# import pandas as pd
# df = pd.read_csv('path/to/your/file.csv')
# print(df.head())
#10.
# - Supervised Learning là phương pháp trong đó mô hình học từ dữ liệu được gán nhãn.
# - Dữ liệu huấn luyện bao gồm các cặp đầu vào và đầu ra.
# - Mục tiêu của Supervised Learning là học một hàm ánh xạ từ đầu vào đến đầu ra.
# - Các thuật toán Supervised Learning bao gồm Linear Regression, Logistic Regression, Support Vector Machines, Neural Networks, và Decision Trees.
# - Unsupervised Learning là phương pháp trong đó mô hình học từ dữ liệu không được gán nhãn.
# - Dữ liệu huấn luyện chỉ bao gồm các đầu vào mà không có đầu ra tương ứng.
# - Mục tiêu của Unsupervised Learning là khám phá cấu trúc ẩn trong dữ liệu.
# - Các thuật toán Unsupervised Learning bao gồm Clustering (K-means, DBSCAN), Dimensionality Reduction (PCA, t-SNE), và Association Rule Mining.
#11.
# I. Thu thập dữ liệu: Thu thập dữ liệu từ các nguồn khác nhau như cơ sở dữ liệu, file CSV, API, web scraping, v.v.
# II. Khám phá dữ liệu: Sử dụng các phương pháp thống kê và trực quan hóa để hiểu cấu trúc, phân phối và các đặc điểm chính của dữ liệu.
# III. Làm sạch dữ liệu: Xử lý các giá trị thiếu, loại bỏ các giá trị ngoại lệ, sửa chữa các lỗi trong dữ liệu, và chuẩn hóa dữ liệu.
# IV. Biến đổi dữ liệu: Chuyển đổi dữ liệu về định dạng phù hợp cho phân tích, bao gồm việc mã hóa các biến phân loại, tạo các biến mới, và chuẩn hóa hoặc chuẩn hóa dữ liệu.
# V. Tích hợp dữ liệu: Kết hợp dữ liệu từ các nguồn khác nhau để tạo ra một tập dữ liệu thống nhất.
# VI. Giảm chiều dữ liệu: Sử dụng các kỹ thuật như PCA để giảm số lượng biến đầu vào, giúp tăng hiệu quả và độ chính xác của mô hình phân tích.
# VII. Chia tách dữ liệu: Chia dữ liệu thành các tập huấn luyện và kiểm tra để đánh giá hiệu suất của mô hình phân tích.
