import re
text = "Punjabi shaa gaye oye"
search = r"Punjabi shaa gaye oye"
match = re.match(search,text)
if match:
   print("Match Found:", match.group())
else:
    print("No Match")   