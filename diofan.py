import math
a=int(input('A= '))
m=int(input('B= '))	
b=int(input('C= '))
def gcd(a,m):
	a=abs(a)
	m=abs(m)
	while a != 0 and m != 0:
		if a > m:
			a = a % m
		else:
			m = m % a
	g=a+m
	return g

g=gcd(a,m)
def qwer(a, m): 
	x = 1 
	x1 = 0
	y = 0
	y1 = 1
	while m != 0:
		q = a// m
		r = a % m
		x2 = x - q * x1
		y2 = y - q * y1
		a, m = m, r
		x, x1 = x1, x2
		y, y1 = y1, y2
	return str(x), str(y)

if a==m==0:
	if b==0:
		print('x and y take any valyes')
	else:
		print('no solutions')
else:
	if b%g != 0:
		print ('no solutions')
	else:
		x0,y0=map(int, qwer(a,m))
		print(x0)
		for n in range(g):
			x=(x0*b)%m
			print(x)
		x0*=a//g
		print('one of the solutions x0=',x0,'y0= ',y0)
		print('general solution: \n x=',x0,'+ (',m//g,'*k) \n y=',y0,'- (',a//g,'*k)')
