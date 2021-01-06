#Coding Challenge 14
#Create a pattern search for plate numbers

import re
pattern = r"[A-Z][A-Z][A-Z]-[0-9][0-9][0-9]"

if re.search(pattern, (input("Enter Plate Number here: "))):
    print("Match Found")
else:
    print("Match not found")
