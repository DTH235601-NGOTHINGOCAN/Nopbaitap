import os

def get_filename(path):
    # Lấy phần tên file kèm đuôi
    return os.path.basename(path)

def get_songname(path):
    # Lấy phần tên file không có đuôi mở rộng
    return os.path.splitext(os.path.basename(path))[0]

# Test
path = "d:\\music\\muabui.mp3"
print(get_filename(path))   # muabui.mp3
print(get_songname(path))   # muabui