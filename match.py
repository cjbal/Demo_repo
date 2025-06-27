import re
text = "Punjabi shaa gaye oye"
search = r"shaa"
match = re.match(search,text)
if search:
   print("Match Found:", match.group())
else:
    print("No Match")   

