import re

pattern = "^The.*Spain$"
txt = "The rain in Spain"
x = re.search(pattern,txt)

if x:
    print("Yes! We have a match")
else:
    print("No match")
    