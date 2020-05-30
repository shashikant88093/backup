x,y=map(int, input().split())
while x < y:
	for i in range(2, x):
		if x==2:
			print(2)
		if x%i==0:
			flag=0
			break
		else:
			flag=1
	if flag==1:
		print(x)
	x=x+1