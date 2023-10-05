#regular expression 
import re


message='My phone number is 98-40031339 & 98-48430749'

#for single data extraction
phoneobj=re.compile(r'\d\d-\d\d\d\d\d\d\d\d')
find=phoneobj.search(message)
print(find.group())

#for all data extraction
print(phoneobj.findall(message))

 