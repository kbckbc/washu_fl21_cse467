import time

CNT = 20

a = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39]
b = [3,7,11,15,19,23,27,31,35,39,43,47,51,55,59,63,67,71,75,79]
c = [2,5,8,11,14,17,20,23,26,29,32,35,38,41,44,47,50,53,56,59]
d = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
e = [10,25,40,55,70,85,100,115,130,145,160,175,190,205,220,235,250,265,280,295]

f = 0
g = 0
tick = 0
tic = time.perf_counter_ns()
for i in range(CNT):
    f = f + a[i] * b[i] + c[i] * d[i] - e[i]
    g = g + (a[i] + d[i]) * (b[i] - c[i]) * e[i]
    tick += 1
toc = time.perf_counter_ns()
print("Tick between the loop is",tick)
print(f"Time gap between the loop is {toc - tic:0.0f} nano seconds")
print(f"One iteration execution time  is {(toc - tic)/CNT:0.0f} nano seconds")

print("Summation of f is",f)
print("Summation of g is",g)
