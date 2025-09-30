import re

def NegativeNumberInStrings(s):
    # Tìm tất cả các số có dấu trừ ở trước
    numbers = re.findall(r'-\d+', s)
    # Chuyển chúng thành kiểu số nguyên
    return [int(num) for num in numbers]

# Ví dụ chạy thử
s = "abc-5xyz-12k91--p"
print(NegativeNumberInStrings(s))  # Output: [-5, -12]