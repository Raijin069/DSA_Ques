def u_cal(u, n):
	temp = u
	for i in range(n):
		temp *= (u + i)
	return temp

def fact(n):
	f = 1
	for i in range(2, n + 1):
		f *= i
	return f

n,x = int(input("no of value")),[]
for i in range(n):
	x.append(float(input("enter x:")))

y = [[0.0 for _ in range(n)] for __ in range(n)]
for i in range(n):
	y[i][0] = float(input("enter y:"))

for i in range(1, n):
	for j in range(n - 1, i - 1, -1):
		y[j][i] = y[j][i - 1] - y[j - 1][i - 1]

for i in range(n):
	for j in range(i + 1):
		print(round(y[i][j],5), end="\t")
	print()

value = float(input("enter the value: "))

sum = y[n - 1][0]
u = (value - x[n - 1]) / (x[1] - x[0])
for i in range(1, n):
	sum += (u_cal(u, i) * y[n - 1][i]) / fact(i)

print('sum = %0.4f' % (sum))