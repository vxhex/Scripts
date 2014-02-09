import sys

try:
    num1 = int(sys.argv[1].translate(None, '-'))
    num2 = int(sys.argv[2].translate(None, '-'))

    for number in range(num1, num2+1):
        phone = str(number)
        print phone[0:3] + '-' + phone[3:6] + '-' + phone[6:10]

except IndexError:
    print "Usage: python " + sys.argv[0] + " START_PHONE END_PHONE"
    print "Generate a list of phone numbers in a given range"
    print "Phone numbers should be of format XXX-YYY-ZZZZ"

