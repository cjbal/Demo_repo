string1 = "Hello"
string2="Punjab"
print(string1 + " " + string2)
text = "Hello Jalamdhar"
strlength = str(len(text))
print ("The Length of string is" + " " + strlength)
uppercasestr = string1.upper()
lowercasestr = string2.lower()
print(uppercasestr)
print(lowercasestr)
newstring=text.replace("Jalamdhar","Kapurthala")
print(newstring)
lateststr=newstring.split()
print(lateststr)
print(lateststr[0])
strung = "  Punjab is Great  "
strip_text = strung.strip()
print(strip_text)
laststring = "Bharat is Great"
newstr2 = "is"
if newstr2 in laststring :
   print ("Punjab" + "and" + laststring)

