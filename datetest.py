from datetime import date
from datetime import datetime

current_date = date.today()
print(current_date)

d_naive = datetime.today()

#textual month, day and year	
date_long = d_naive.strftime("%B %d, %Y")

print(date_long)