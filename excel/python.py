import csv
import sys
from datetime import datetime

FIELD = 1
FMT = '%d/%m/%Y'

readablefile = csv.reader(sys.stdin)
writablefile = csv.writer(sys.stdout)
for column in readablefile:
    print("done")
    dt = datetime.strptime(column[FIELD], FMT)
    column[FIELD] = dt.isoformat()
    writablefile.writerow(column)
 
print("program completed")