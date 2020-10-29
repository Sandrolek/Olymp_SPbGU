import math

n=int(input())

radius={}

if n<5:
    print(1)
else:
    for a in range(3,n):
        for b in range(a+1,n):
            c=math.sqrt(a**2+b**2)
            if c<=n:
                
                if c==int(c):
                    #print(f"A: {a}, B: {b}, C: {c}")
                    c=int(c)
                    if c not in radius.keys():
                        radius[c]=1
                    else:
                        radius[c]+=1
    #print(radius)            
    max_r=max(radius)
    print(max_r)
