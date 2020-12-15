import re
emailAddress = input()
emailreg = "(\w+)@((\w+\.)+(com))"
r2 = re.match(emailreg,emailAddress)
print(r2.group(1))
s = input()
print(re.findall("\d+",s))
