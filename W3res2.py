"""fname=input("give 1st name: ")
lname=input("give ur last name: ")
print("hello ",lname,fname)
#list and tuple gen
values=input("give values with commas: ")
list=values.split()
tuple=tuple(list)
print("list: ",list)
print("Tuple ",tuple)
filename=input("enter ur filename: ")
ext=filename.split(".")
print("ext of flname is: ",str(ext[-1]))
list=['red','green','black','blue']
print("1st color: ",list[0],"last colour: ",list[-1])
#exam schedule format
exam_st_date=(11,12,2026)
print("EXAM IS ON: %i/%i/%i " % exam_st_date)
#num expansion cal
n=int(input("Enter no: "))
n1=int("%s"%n)
n2=int("%s%s"%(n,n))
n3=int("%s%s%s"%(n,n,n))
print("EXPANSION OF NO: ",n1+n2+n3)
#func documentation printer
print(len.__doc__)
print(sorted.__doc__)
print(sum.__doc__)
print(abs.__doc__)
#monthly calendar display
import calendar
y=int(input("Enter year to see calen: "))
m=int(input("Enter month of yr to see: "))
print("Calendar: ",calendar.month(y,m))"""
#days bet dates
from datetime import date
fd=date(2026,3,31)
ld=date(2026,5,29)
diff = ld-fd
print("days= ",diff.days)