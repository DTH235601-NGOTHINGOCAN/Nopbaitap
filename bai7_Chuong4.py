from math import sqrt
print("Nhap toa do A: ")
xA = float(input("Nhap X: "))
yA = float(input("Nhap Y: "))
print("Nhap toa do B: ")
xB = float(input("Nhap X: "))
yB = float(input("Nhap Y: "))
DoDai = sqrt((xB - xA)**2+ (yB-yA)**2)
print("Doan AB co do dai:  ", DoDai)
