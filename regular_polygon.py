import math

N = int(input())
R = 4.5
for i in range(N):
    x, y = R+R*math.cos(2*math.pi*i/N), R+R*math.sin(2*math.pi*i/N)
    print("(%.2f,"%x, "%.2f)"%y)
