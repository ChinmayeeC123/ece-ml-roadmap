"""cities=["banglore","delhi","udaipur","mysore","chennai"]
heros=["red","black","white","blue"]

def print_len(list):
    print(len(list))
    
print_len(heros)    
print_len(cities)
print(heros[0],end=" ")#end="\n"
print(heros[1],end=" ")#" "is given to print in same line

def print_list(list):
        for item in list:
              print(item, end=" ")#end="\n"all items in next line all different lines

print_list(cities)
print_list(heros)       """  

"""n=int(input("Enter ahn no:"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact) 
x=int(input("Enter fac no:"))
def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
    print(fact)   
cal_fact(x)
n=float(input("Enter usd val:"))
def converter(usd_val):
    inr_val=usd_val*91.63
    print(f"Todays inr val is {inr_val} and usd val is {usd_val}") 

converter(n)"""
#print n to 1
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)

def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(5))    
    
def sums(n):
    if(n==0 ):
        return 0
    return sums(n-1)+n
print(sums(10))

def listss(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    listss(list,idx+1)

fruits=["mango","apple","cat"]    
listss(fruits)