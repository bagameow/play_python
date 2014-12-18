import re

def printTest(str):
    print str
    return str

file = open("parsed.xml", "r")
#content = file.read()
#print content
#file.close()
i = 1
startNote = 0
while True:
    line = file.readline()
    if not line: break
    if i > 1000: 
        break
    i = i + 1
    if startNote == 1:


    m = re.search("<FormattedID>(.*)</FormattedID>" , line)
    if m is not None: 
        print m.group(1),
    else:
        m = re.search("<Notes>(.*)$", line)
        if m is not None:
            startNote = 1
            print "note found: " + m.group(1)



file.close()




