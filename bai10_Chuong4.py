import time
import os

# Hàm xóa màn hình (dùng cho Windows, nếu bạn dùng Mac/Linux thì thay 'cls' thành 'clear')
def clear():
    os.system('cls')  # hoặc 'clear' nếu không dùng Windows

# Danh sách các hình cần vẽ
hinh1 = """
        *
        * *
        * * * 
  * * * * * * *
  * * * 
  * *
  *
"""

hinh2 = """
   
        *
        * *
        *   * 
  * * * * * * *
  *   * 
  * *
  *
"""

hinh3 = """
      * * * * 
      * * *
      * *
      *
    * *
  * * * 
* * * *
"""

hinh4 = """
      * * * * 
      *   *
      * *
      *
    * *
  *   * 
* * * *
"""

# Vẽ từng hình cách nhau 5 giây
for hinh in [hinh1, hinh2, hinh3, hinh4]:
    clear()
    print(hinh)
    time.sleep(5)

clear()
print("Kết thúc chương trình!")