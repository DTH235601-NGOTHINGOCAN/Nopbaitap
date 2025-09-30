import math
try:
	r= float (input(' Nhap ban kinh hinh tron: '))
	print('Ban kinh hinh tron: ', r)
	cv= 2*math.pi*r
	dt= r**2
	print(' Chu vi la:', cv)
	print('Dien tich la:', dt)
except:
		print(' Loi roi! ')