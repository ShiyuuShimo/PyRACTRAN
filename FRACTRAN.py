import sys

args = sys.argv

path = args[1]
kinput = args[2]
k = int(kinput)
step = 0

with open(path, mode='r') as c:
	source = c.read()
	code = [[int(x) for x in y.split('/')] for y in source.split()]

while True:
	for n in range(len(code)):
		
		if k % code[n][1] == 0:
			k = k * code[n][0] // code[n][1]
			step += 1
			print(f'step {step}')
			print(k)
			break

	else:
		break

print(f'finished. {k}')
