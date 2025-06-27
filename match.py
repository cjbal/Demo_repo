import re
text = "Punjabi shaa gaye oye"
search = r"shaa"
match = re.match(search,text)
if match:
   print("Match Found:", match.group())
else:
    print("No Match")   

