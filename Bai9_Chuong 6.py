# Hàm kiểm tra số nguyên tố
def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Nhập mảng (có thể sửa thành input từ bàn phím)
M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]

# Số lẻ
so_le = [x for x in M if x % 2 == 1]
print("Dòng 1 - Các số lẻ:", so_le, f"→ Có {len(so_le)} số lẻ")

# Số chẵn
so_chan = [x for x in M if x % 2 == 0]
print("Dòng 2 - Các số chẵn:", so_chan, f"→ Có {len(so_chan)} số chẵn")

# Số nguyên tố
so_nt = [x for x in M if la_nguyen_to(x)]
print("Dòng 3 - Các số nguyên tố:", so_nt)

# Không phải số nguyên tố
khong_nt = [x for x in M if not la_nguyen_to(x)]
print("Dòng 4 - Không phải số nguyên tố:", khong_nt)
