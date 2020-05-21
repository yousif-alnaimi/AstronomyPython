# Usage is: "python RA_Dec_to_Decimal.py [RA (with spaces between numbers)] [DEC (with spaces between numbers)]
# e.g. python RA_Dec_to_Decimal.py 18 36 56 38 47 1

import sys
import numpy

val1 = sys.argv[1]
val2 = sys.argv[2]
val3 = sys.argv[3]
val4 = sys.argv[4]
val5 = sys.argv[5]
val6 = sys.argv[6]

RA = (float(val1) / 24 + float(val2) / 1440 + float(val3) / 86400) * 360
DEC = float(val4) + float(val5)/60 + float(val6)/3600

RA_2dp = round(RA, 2)
DEC_2dp = round(DEC, 2)

print(str(RA_2dp) + ", " + str(DEC_2dp))
