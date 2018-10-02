import re
mail='murali.thirumur@gmail.com,asgpriya25@yahoo.com,raymondcy95@gmail.com,murali.s@pfizer.com'
result=re.findall('\w+@([a-zA-Z]+)',mail)
print (result)
