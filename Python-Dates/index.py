# Example
# Return the year and name of weekday:

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Example
# Create a date object:

x = datetime.datetime(2020, 5, 17)
print(x)