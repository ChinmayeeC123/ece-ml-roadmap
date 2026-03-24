"""list1=[54,87,9]
list1.append(49)
list1.sort()
print(list1)
print(list1.sort(reverse=True))
list1.insert(2,26)
print(list1)
list2=[2,1,5,1]
list2.remove(1)#remove 1
list2.pop(0)#pop at index 2
print(list2)
print(type(list2))
print(list1+list2)

tup=(1,2,3,2,2)
print(tup.index(2))#2 no index is 1 atkes 1st index
print(tup.count(2))
print(tup[1:3])
print(tup[-3:-1])
mov =[]
mov1,mov2,mov3=input("ENTER UR FAV MOVIES: with space ").split()
mov.append(mov1)
mov.append(mov2)
mov.append(mov3)
print(mov) 
movie=[]
movie.append(input("ENTER 1ST MOVIE "))
movie.append(input("ENTER 2ND MOVIE "))
movie.append(input("ENTER 3RD MOVIE "))
print(movie) 
list=["M","A","A","M"]
coplist=list.copy()
coplist.reverse()
if(coplist==list):
    print("IS PALI")
else:
    print("IS NOT PAL")
STD=["A","D","C","A","F","C","B","A","B"]
print(STD.count("A"))
STD.sort()
print(STD)
print(len(STD))
print(f"LAST 3 NUM{STD[-3:]}")
cart = ["milk", "bread", "eggs"]
prices = [50, 30, 20]
total = sum(prices)
print(f"Total: ₹{total}")

# Q8: Largest number in list
numbers = list(map(int, input("Enter 5 numbers: ").split()))
largest = max(numbers)
print(f"Largest: {largest}")

# Q9: Count occurrences
grades = [85, 92, 85, 78, 92]
unique_grades = set(grades)
print(f"Unique grades: {list(unique_grades)}")
#loops for
movies=[]
for i in range(4):
    movie=input(f"ENTER {i+1} MOVIE: ")
    movies.append(movie)
    print(f"YOUR FAV MOV ARE:{movies}")"""
person = ("Arjun", 20, ("ECE", "VTU"))
name, age, (branch, uni) = person
print(f"{name}, {age}, {branch} {uni}")
#CONVERT LIST TO TUPLE
shopping_list = ["milk", "bread", "eggs"]
shopping_tuple = tuple(shopping_list)
print(f"Tuple: {shopping_tuple}")

 


