# 1.B
# 2.A
# 3.B
# 4.C
# 5.A
# 6.A
# 7.B
# 8.D
# 9.C
# 10.A
# 11.A
# 12.A
# 13.B
# 14.A
# 15.B
# 16.A
# 17.A
# 18.B
# 19.A
# 20.A

def epj(q, j):
    q.append(j)

def dpj(q):
    if q:
        return q.pop(0)
    else:
        return "Không có tác vụ nào trong hàng đợi"


pq = []
epj(pq, "Văn bản 1")
epj(pq, "Văn bản 2")
epj(pq, "Văn bản 3")

while pq:
    cj = dpj(pq)
    print(f"Đang in: {cj}")


# def rcm(st,m):
#     st.append(m)
# def um(st):
#     if st:
#         return st.pop(-1)
#     else:
#         return "ko co gi"
# mt=[]
# rcm(mt,"run")
# rcm(mt,"jump")
# rcm(mt,"fly")
# print(mt)
# lm=um(mt)
# print(lm)
# print(mt)
