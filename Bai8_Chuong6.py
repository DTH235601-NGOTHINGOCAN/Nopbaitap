# Nhập số phần tử
n = int(input("Nhập số phần tử n: "))

# Nhập dãy số thực
M = []
for i in range(n):
    x = float(input(f"Nhập M[{i}]: "))
    M.append(x)

# Sắp xếp giảm dần
M.sort(reverse=True)

# Xuất kết quả
print("Dãy số sau khi sắp xếp giảm dần:", M)
