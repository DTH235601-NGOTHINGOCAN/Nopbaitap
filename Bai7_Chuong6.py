def nhap_day_tang():
    n = int(input("Nhập số phần tử của dãy: "))
    lst = []
    
    for i in range(n):
        while True:
            x = int(input(f"Nhập phần tử thứ {i+1}: "))
            # Kiểm tra điều kiện tăng dần
            if i == 0 or x > lst[-1]:
                lst.append(x)
                break
            else:
                print("❌ Số vừa nhập không lớn hơn phần tử trước đó. Vui lòng nhập lại!")
    
    return lst


# Chạy chương trình
day = nhap_day_tang()
print("✅ Dãy số đã nhập:", day)