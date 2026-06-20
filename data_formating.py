#Time between two date-times
from datetime import datetime
a = datetime(2016,10,06,0,0,0)
b = datetime(2016,10,01,23,59,59)
a-b
# datetime.timedelta(4, 1)
(a-b).days
# 4
(a-b).total_seconds()
# 518399.0
#Parsing string to datetime object
from datetime import datetime
datetime_string = 'Oct 1 2016, 00:00:00'
datetime_string_format = '%b %d %Y, %H:%M:%S'
datetime.strptime(datetime_string, datetime_string_format)
# datetime.datetime(2016, 10, 1, 0, 0)
