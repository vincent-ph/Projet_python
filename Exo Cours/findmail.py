import re
mail = "vincent@hotmail.com"
regex = r'.+\.\w{1,3}\b'

if "@" and "." in mail and re.match(regex, mail):
    print("Email OK")
else:
    print("Ce n'est pas un mail correct")
