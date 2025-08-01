num=19
while num>1:
    res=0
    while num!=0:
        id=num%10
        res+=id**2
        num=num//10
    num=res
if num ==1 or num == 7:
    print('happy number')
else:
    print('not happy number')
