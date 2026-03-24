"""list=[]
print(list)
i=1
while i<=10:
  sq=i*i
  print(sq)
  i+=1
  list.append(sq)

print(list) 
tup=(1,4,9,16,25,36,49,64,81,100)
X=9
i=0
while i < len(tup):
    if(tup[i]==X):
        print("no found at indx ",i, " num is ",tup[i])
        break
    else:
        print("finding")
    i+=1 
i=1
while i<=10:
    if(i%2==0):
        i+=1
        continue#skip
    print(i)
    i+=1

i=0
while i <= 5:
    if(i==3):
        i+=1
       # continue
        
    print(i) 
    i+=1  
str="apnacollege"

for char in str:
    if(char == 'o'):
        print("o found")
        break
    print(char)
else:
    print("end")
list=[]
for i in range(0,11,1):
    sq=i*i
    print(sq)
    list.append(sq)
    i+=1
print(list) 
tup=()
tup=tuple(list)
print(tup) 
X=36
idx=0
for num in tup:
    if(num == X):
        print("no is ",num," found at index ",idx) 
        break
    idx+=1

else:
        print("finding...")"""
"""n=int(input("Enter no:"))
i=1
sum=0
while i<=n:
    #print(i)
    sum=sum + i
    i += 1
print(sum)    """
n=int(input("Enter no:"))
i=1
fact=1
while i<=n:
    #print(i)
    fact=fact * i
    i += 1
print(f'factorial is:{fact}')    




