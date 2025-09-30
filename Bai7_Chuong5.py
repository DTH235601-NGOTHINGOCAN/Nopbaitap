def OptimizeName(s):
    # Xóa khoảng trắng thừa ở đầu và cuối, tách các từ
    words = s.strip().split()
    # Viết hoa chữ cái đầu, còn lại viết thường
    words = [w.capitalize() for w in words]
    # Ghép lại thành chuỗi
    return " ".join(words)

# Test
s = "   TRầN   duY   thAnH   "
print(OptimizeName(s))  # Output: Trần Duy Thanh