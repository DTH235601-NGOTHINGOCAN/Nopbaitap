import unicodedata

# Hàm loại bỏ dấu tiếng Việt để dễ kiểm tra nguyên âm
def remove_accent(ch):
    nfkd = unicodedata.normalize('NFD', ch)
    return ''.join(c for c in nfkd if not unicodedata.combining(c))

def analyze_string(s):
    uppercase = lowercase = digits = special = spaces = vowels = consonants = 0
    vowel_set = set("aeiouy")   # Nguyên âm cơ bản (coi cả y là nguyên âm)

    for ch in s:
        if ch.isupper():
            uppercase += 1
        if ch.islower():
            lowercase += 1
        if ch.isdigit():
            digits += 1
        if ch == " ":
            spaces += 1
        if not ch.isalnum() and not ch.isspace():
            special += 1
        if ch.isalpha():  # Nếu là chữ cái
            base = remove_accent(ch).lower()
            if base in vowel_set:
                vowels += 1
            else:
                consonants += 1

    print("Số chữ IN HOA:", uppercase)
    print("Số chữ in thường:", lowercase)
    print("Số chữ số:", digits)
    print("Số ký tự đặc biệt:", special)
    print("Số khoảng trắng:", spaces)
    print("Số nguyên âm:", vowels)
    print("Số phụ âm:", consonants)

# =============================
# Chạy thử
text = input("Nhập chuỗi: ")
analyze_string(text)
