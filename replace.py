import re
text = "Punjabi Shaa Gaye Oye"
pattern = r"Shaa"
replacement = "Aa"
newtext = re.sub(pattern,replacement,text)
print(newtext)