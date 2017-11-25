def tri(x):
	i,n,a=0,0,[0,1,0]
	while n<x:
		yield(a[1:-1])
		a=[0]+[a[i]+a[i+1] for i in range(n+2)]+[0]
		n+=1
for m in tri(3):
	print(m)