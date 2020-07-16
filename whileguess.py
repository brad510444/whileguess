import random
start = input('請輸入初始值')
end = input('請輸入結束值')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1 #count = count + 1
	n = input('請輸入號碼: ')
	n = int(n)
	if n == r: #要加冒號
		print('恭喜你猜對了！')
		print('這是你猜的第', count,'次')
		break
	elif n > r:
		print('比答案大')
	else:
		print('比答案小')
	print('這是你猜的第', count,'次')