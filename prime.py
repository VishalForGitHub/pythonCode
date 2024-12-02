n=3
f=1
for i in range(2,n):
    if(n%i==0):
        f=0
        break

print('no is prime') if f==1 else print('not prime')
