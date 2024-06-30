def mean(d):
    val=0
    for i in d:
        val+=i
    val/=(d.__len__())
    return val
def median(d):
    l=d.__len__()
    if l%2==0:
        val=(d[(l-1)//2]+d[(l+1)//2])/2
    else :
        val=d[l//2]
    return val
def mode(d):
    l=[]
    count=0
    for i in range(0,d.__len__()):
        count=d.count(d[i])
        l.append([i,count])
    val=l[0][1]
    for i in range(0,l.__len__()):
        val=max(val,l[i][1])
    return d[val]


data=input().split(',')
for i in range(0,data.__len__()):
    data[i]=int(data[i])
data.sort()
result=[data[0],data[-1],mean(data),median(data),mode(data)]
print(result)
