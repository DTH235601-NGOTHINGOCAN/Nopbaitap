def number_to_vietnamese(n):
    if not (0 <= n <= 99):
        return "Ngoài phạm vi (0..99)."

    words = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

    if n < 10:
        return words[n]

    tens = n // 10
    unit = n % 10

    if tens == 1:
        # 10..19
        if unit == 0:
            return "mười"
        if unit == 5:
            return "mười lăm"
        return "mười " + words[unit]

    # tens >= 2
    tens_word = words[tens] + " mươi"

    if unit == 0:
        return tens_word
    if unit == 1:
        return tens_word + " mốt"
    if unit == 4:
        return tens_word + " bốn"   # có thể đổi thành "tư" nếu muốn
    if unit == 5:
        return tens_word + " lăm"
    return tens_word + " " + words[unit]


# Thử nghiệm:
for x in [0, 5, 10, 11, 15, 20, 21, 24, 25, 30, 35, 40, 44, 50, 55, 99]:
    print(x, "=>", number_to_vietnamese(x))