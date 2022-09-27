#written by Jorge Rea
# Create a Python program called "Character Analyzer" that will prompt the user for a integer. 
# the program will return the ascii character 
# Finally the program should print the
# ASCII number in decimal and hexadecimal.
# The opposite case (e.g. upper -> lower or lower -> upper) version of the character if it is a letter.
# If the character is a vowel or a control character.
# The program should print a friendly message if the character cannot be printed (non-printable).
# When finished, submit your Python source code (the .py file) below.

# put constants here



# do inpoutting here
user_input = int(input("Please enter the integer value of the ascii character to analyze"))
if user_input <0 or user_input > 126:
    print("not a valid number man")
    exit()

#do processing here
# figure if "control character"... 
if user_input >= 0 and user_input <=31:
    print("This is a control character and cannot be printed")
# Figure if "space character"
elif user_input == 32:
    print("This is a space character:__")
#figure if "special character".....
elif 33 <= user_input <= 47 or 123<= user_input <= 126 or 58 <= user_input <= 64 or 91<= user_input<= 96: # only python lets you do this crap
    print("This is a special character:",chr(user_input))
#figure if " ascii digits"
elif chr(user_input) >= '0' and chr(user_input) <= '9':
    print("it worked!!!",chr(user_input))
#figure if "uppercase letter"
elif user_input >= 65 and user_input<= 90:
    print("This is upper character and here is the lower case value:",chr(user_input).lower())
#figure if "lowercase letter"
elif user_input >= 97 and user_input <= 122:
    print("This is lower character and here is the upper case value:",chr(user_input).upper())
else: 
    print("Not in the ASCII table !!")


#comments : when i tried 52 it gave me back 52
#never mind i just didnt start the program









# do outputting here












































