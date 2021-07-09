n=input('輸入人數')
n=int(n)
sum=0
max=0
min=0
for x in range(0,n):
    y=input('請輸入分數' + str(x+1) + ':')
    y = int(y)        
    sum=sum+y
    if max>y:
        max=max
    else:
        max=y
    if min>y:
        min=y
    else:
        if min==0:
           min=y
        else:
           min=min           
            
print('平均分數=' + str(int(sum/n)))
print('最大分數=' + str(max))
print('最小分數=' + str(min))