import re
text = "Punjab is great"
pattern = r"great"
search = re.search(pattern,text)
if search:
    print("Punjab is great")
else:
    print("Udta Punjab")    