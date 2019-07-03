import math

opp = int(raw_input())
adj = int(raw_input())

TOA = opp/adj

print str(int(round(math.degrees(math.atan(TOA)))) + "°")
