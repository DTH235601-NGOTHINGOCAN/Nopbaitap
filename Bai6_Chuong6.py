import random

# Nhập số phần tử cần tạo
N = int(input("Nhập số phần tử N: "))

# Sinh ra list gồm N số ngẫu nhiên KHÔNG TRÙNG NHAU trong khoảng [-100, 100]
lst = random.sample(range(-100, 101), N)

print("List ngẫu nhiên:", lst)