import re
text = "Punjab is great"
pattern = r"greater"
search = re.search(pattern,text)
if search:
    print("Punjab is great")
else:
    print("Udta Punjab")    