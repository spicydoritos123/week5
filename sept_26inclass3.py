# #telephone company
# Write a program that calculates and prints the bill for a cellular telephone company.  The company offers two types of service: regular and premium. Its rates vary, depending on the type of service. The rates are computed as follows:
 # Regular Service:  
# $10.00 plus
# First 50 minutes are free, over that, $0.20 per minute.
# Premium service:  
# $25.00 plus
# For calls made from 6:00 a.m. to 6:00 p.m., 
# the first 75 minutes are free, over that, $0.10 per minute.
# For calls made from 6:00 p.m. to 6:00 a.m., 
# the first 100 minutes are free, over that, $0.05 per minute.
# Your program should prompt the user to enter an account number, 
# a service code, and the number of minutes the service was used. 
# A service code of r or R means regular service; a service code of p or P means premium service. 
# Treat any other character as an error. 
# Your program should output the account number, type of service, 
# number of minutes the telephone service was used, and the amount due from the user.
# For the premium service, the customer may be using the service during the day and the night. 
# Therefore, to calculate the bill, you must ask the user to input the number of minutes the service was used 
# during the day and the number of minutes the service was used during the night.
# When finished, submit your Python source code (the .py file) below.

#put constants here 
PLAN_FEE = float(25)    

# do inputting here
acct_num = input("Please enter your account number:")
minutes_day = int(input("Please enter the number of minutes used during the day:"))
minutes_evening = int(input("Please enter the number of minutes used in the evening"))

# do processing here
day_time_charge = 0
if minutes_day > 75:
    day_time_charge = (minutes_day - 75) * .10

nighttime_charge = 0
if minutes_evening > 100:
    nighttime_charge = (minutes_evening - 100) * .05

total = day_time_charge + nighttime_charge + PLAN_FEE

# do outputting here
print("The total for account:",acct_num,"is:${:.2f}".format(total))




