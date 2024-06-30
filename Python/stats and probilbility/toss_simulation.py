import random
def g():
    heads=0
    for i in range(100):
        if random.random()<=0.5:
            heads+=1
    return heads
def sim(n):
    list=[]
    for i in range(n):
        list.append(g())
    return (sum(list)/n)

print(sim(10))
print(sim(100))
print(sim(1000))
print(sim(10000))
print(sim(100000))