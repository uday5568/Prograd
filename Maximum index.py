steps = int(input())
badElement = int(input())
i,j,p,q=(0,1,0,2)
while(steps):
    steps-=1
    if(j!=1):
        if( p+q!=badElement):
            p+=q
        q+=1
    if(i+j!=badElement):
        i+=j
    j+=1
print(max(i,p))