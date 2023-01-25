import readfile
import re
from datetime import datetime
  
# initializing string
test_str = "gfg at 2021-01-04"
  
# printing original string
print("The original string is : " + str(test_str))
  
# searching string
match_str = re.search(r'\d{4}-\d{2}-\d{2}', test_str)
  
# computed date
# feeding format
res = datetime.strptime(match_str.group(), '%Y-%m-%d').date()
  
# printing result 
print("Computed date : " + str(res)) 