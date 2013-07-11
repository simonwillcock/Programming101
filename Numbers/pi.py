# Round Pi to the number of digits set by the user (max 20)

from math import pi

digits = int(raw_input("How many decimal places of Pi should display: "))

print(("{0:.%df}" % min(20,digits)).format(pi))