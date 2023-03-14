# Python3 Program to interpolate using
# newton backward interpolation

# Calculation of u mentioned in formula
def u_cal(u, n):
	temp = u
	for i in range(n):
		temp = temp * (u + i)
	return temp

# Calculating factorial of given n
def fact(n):
	f = 1
	for i in range(2, n + 1):
		f *= i
	return f


# Driver code


# number of values given
n = 7
x = [1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30]

# n = 5
# x = [1891, 1901, 1911, 1921, 1931]

# y is used for difference
# table and y[0] used for input
y = [[0.0 for _ in range(n)] for __ in range(n)]
y[0][0] = 2.7183
y[1][0] = 2.8577
y[2][0] = 3.0042
y[3][0] = 3.1582
y[4][0] = 3.3201
y[5][0] = 3.4903
y[6][0] = 3.6693

# Calculating the backward difference table
for i in range(1, n):
	for j in range(n - 1, i - 1, -1):
		y[j][i] = y[j][i - 1] - y[j - 1][i - 1]


# Displaying the backward difference table
for i in range(n):
	for j in range(i + 1):
        # pass
        # print('%0.4f' % (y[i][j]))

		print(round(y[i][j],5), end="\t")

	print()

# Value to interpolate at
value = 1.35

# Initializing u and sum
sum = y[n - 1][0]
u = (value - x[n - 1]) / (x[1] - x[0])
for i in range(1, n):
	sum = sum + (u_cal(u, i) * y[n - 1][i]) / fact(i)

# print("\n Value at", value, "is", sum)
print('sum = %0.4f' % (sum))



# This code is contributed by phasing17
