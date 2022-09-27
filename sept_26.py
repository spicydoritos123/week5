# written by Jorge Rea
# Spherical Inc. sells baseballs for $1.99 each. However, discounts are given according quantities listed in the following table:

# Quantity	Discount
# 0 - 9	0%
# 10 - 50	5%
# 51 or more	10%
 

# Develop a Python program that prompts the user to enter the number of baseballs purchased.
# The program should ask the user if they want giftwrapping and if so add another $2.00 to the order.
# The program should display the amount of the discount (if any) and the total amount of the purchase after the discount and including the giftwrapping if needed.
# Include tax of 6% on the total of the purchase, excluding giftwrapping.
# When finished, submit your Python source code (the .py file) below.
# Notes:

# Your program must include comments describing the important parts.
# The program's UI/UX should be clean and intuitive.
# There should be no "magic numbers" in your program.
# Only use code that has been discussed in this class (e.g. no functions, loops, etc. unless otherwise indicated).
# This assignment must be done in class to receive credit.


#name contants here
from operator import truediv


BASEBALL_PRICE = 1.00 #FIXME
GIFT_WRAP      = 2.00
TAX            =  .06

DISCOUNT_5     =  .05
DISCOUNT_10    =  .10
#do inputting here
#BASEBALL_QTY   = int(input"Please enter the number of baseballs you would like to purchase")
BASEBALL_QTY = 100  #FOR DEBUGGING ONLY

#GIFT_WRAPPING = input("Would you like Gift Wrapping for an additional $2.00? (y/n) ")
GIFT_WRAPPING = 'y'
if BASEBALL_QTY < 0:
    print("what is that???")
#do processing here
the_discount = 0

#figuring out what discount to give if any

if BASEBALL_QTY <= 9:
    #STASH DISCOUNT
    the_discount = 0
elif BASEBALL_QTY > 9 and BASEBALL_QTY <= 50:
    #STASH DISCOUNT
    the_discount = DISCOUNT_5
else:
    #stash discount
    the_discount = DISCOUNT_10

#calculating discount
SUB_TOTAL = BASEBALL_QTY * BASEBALL_PRICE 
DISCOUNT_TOTAL = SUB_TOTAL * the_discount
PRE_TAX_TOTAL = SUB_TOTAL - DISCOUNT_TOTAL
TAXED_TOTAL = (PRE_TAX_TOTAL * TAX) + PRE_TAX_TOTAL
#figure out gift wrapping
GRAND_TOTAL = TAXED_TOTAL
if GIFT_WRAPPING == 'y':
    GRAND_TOTAL = GIFT_WRAP + TAXED_TOTAL



# do outputting here
print("Your total for the baseballs is:",GRAND_TOTAL )
# STOP THE PROGRAM
input("press enter to exit program")




















