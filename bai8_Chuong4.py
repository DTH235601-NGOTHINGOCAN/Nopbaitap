import math

while True:
    # Nhập cơ số a
    a = input("Nhập cơ số a (a > 0, a != 1: ")
    if a.lower() == "q":
        print("Kết thúc chương trình!")
        break
    a = float(a)

    # Kiểm tra a hợp lệ chưa
    if a <= 0 or a == 1:
        print("❌ Lỗi: a phải > 0 và a != 1")
        continue

    # Nhập x
    x = input("Nhập giá trị x (x > 0): ")
    if x.lower() == "q":
        print("Kết thúc chương trình!")
        break
    x = float(x)

    # Kiểm tra x hợp lệ chưa
    if x <= 0:
        print("❌ Lỗi: x phải > 0")
        continue

    # Tính log_a(x)
    result = math.log(x) / math.log(a)
    print(f"✅ log_{a}({x}) = {result}\n")