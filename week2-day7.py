"""color=input("Enter traff color:")
if(color=="red"):
    print("STOP")
elif(color=="YELLOW"):
    print("STEADY")
else:
    print("GO")
ann=float(input("Enter ur family NNUAl income:"))
marks=float(input("ENTER UR MARKS"))
if(marks>=90 and ann<=100000):
    print("FULL SCOHLARE")
elif(marks>=75 and ann<=200000):
    print("HALF SCH")
else:
    print("invalid")
is_member = input("Enter T/F: ").upper().startswith('T')
loyalty_points = int(input("Enter loyalty points:"))
if not is_member and loyalty_points >= 100:
    print("Join membership offer")
elif  is_member or loyalty_points >= 200:
    print("VIP discount")
else:
    if not (not is_member and loyalty_points >= 100):
        print("Standard pricing")"""
age=int(input("Enter ur age:"))
time=input("Enter show time:matinee/night:")
if age<=12:
    price=100 if time == "matinee" else 150
elif age<=60:
    price=200 if time == "night" else 170
else:
    price=150

print(f"TICKET: rup {price}")           