import re
text = "Pattern Bole Soh Nihal"
pattern = r" "
splitresult = re.split(pattern, text)
print(splitresult)
print(splitresult[1,2,3])