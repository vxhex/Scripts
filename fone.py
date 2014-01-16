import sys

try:
    num1 = sys.argv[1].split('-')
    num2 = sys.argv[2].split('-')

    for area in range(int(num1[0]), int(num2[0])+1):
        for prefix in range(int(num1[1]), int(num2[1])+1):
            for line in range(int(num1[2]), int(num2[2])+1):
                print str(area).zfill(3) + '-' + str(prefix).zfill(3) + '-' + str(line).zfill(4)

except IndexError:
    print "Usage: python " + sys.argv[0] + " START_PHONE END_PHONE"
    print "Generate a list of phone numbers in a given range"
    print "Phone numbers should be of format XXX-YYY-ZZZZ"

