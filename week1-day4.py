"""dict={"key":"values",
      "name":"Chinmayee",
      "sub":{ "phy":92,"chem":94,"bio":100},
      "12.99":14,
      "marks":[1,2,3,4]}
print(type(dict))
print(dict["name"])
dict["name"]="APNA"
dict["CGPA"]=9.5
print(dict)
print(dict["sub"]["chem"])
print(list[dict.keys()])
print(list[dict.values()])
pairs=list(dict.items())
print(pairs)
print(pairs[2])
print(dict.get("key"))
newdict={"city":"banglore"}
print(dict.update(newdict))
print(dict) 
set={1,2,2,"hell","wolf","wolf",4}
print(set)
print(len(set))
set.add("nam")
set.add(23)
#set.add(1,6,7) this is list so cant add errror wil come
set.add((1,3,8))#it is tuple
set.remove(2)
print(set)
set.pop() #pops random value
print(set)
set.clear()
print(set)
set1={1,2,3}
set2={2,3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))
pyth={}
#pyth["table"]="snma furni","tab"
#pyth["cats"]="small anmi"
print(pyth)
phy=input("enter phy marks:")
chem=input("enter chem marks:")
bio=input("enter bio marks:")
pyth["phy"]=phy
pyth["chem"]=chem
pyth["bio"]=bio
print(pyth)"""
set={9,9.0}
print(set)
set={9,"9.0"}
print(set)
set={"9",9.0}
print(set)
set={("int",9),("float",9.0)}
print(set)