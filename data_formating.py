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
