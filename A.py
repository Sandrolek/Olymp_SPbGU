h,t,a,b,c = [int(i) for i in input().split()]

print("Started")

bites = 0
killed = False

if c>a:
    while h+t >= c:
        #print("H:",h,"T:",t)
        if h>=c:
            h=h-c+a

        bites+=1
        
        if h<c and h+t>=c:
            killed = True
            print(bites)
            break
        
if not killed:
    print(-1)
