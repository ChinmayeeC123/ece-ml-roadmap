print("Twinkle,twinkle little star,\n\t\t How i wonder wonder what you are!\n\t\t\tUP abover d world so high ,\n \t\t\tLike a diaMOND IN D SKY.")
#python version checker
import sys 
print("PYTHON VERSION: ",sys.version,"VERSION INFO: ",sys.version_info)
#print current datetime
import datetime
print("CURRENT TIME AND DATE: ")
now=datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
#CIRCLE ARE CAL
r=float(input("give radius:"))
print("AREA IS: ",r*r*3.14)