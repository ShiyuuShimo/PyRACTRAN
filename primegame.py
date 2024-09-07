k = int(input('enter natural number. '))

a, b = k + 1, k

while True:
	if a % b != 0:
		b -= 1
	elif b > 1:
		a += 1
		b = a - 1
	else:
		print(a)
		break
