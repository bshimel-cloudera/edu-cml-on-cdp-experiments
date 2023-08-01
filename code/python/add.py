import sys

params = [int(number) for number in sys.argv[1:]]
total = sum(params)

print (f"The sum of the numbers is: {total}")