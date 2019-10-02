b=0
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
for i in range(0,n):
    for j in range(0,n-1):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1], a[j]
            b = b+1
    if(b==0):
        break;
print("Array is sorted in", b , "swaps.")
print("First Element:", a[0])
for i in range(0, len(a)): 
  
    if i == (len(a)-1): 
        print ("Last Element:" ,  a[i]) 
