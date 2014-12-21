# coding=UTF-8
# -*- coding: <encoding name> -*-

import re


def deal_with_note(l):

    global startNote

    m = re.search("(.*)</Notes>", l)
    if m is not None:
        s = m.group(1)
        print s.replace(",", "，")
        startNote = 0
        return
    else:
        print l.replace(",", "，")


myFile = open("parsed.xml", "r")
i = 1
startNote = 0
while True:
    line = myFile.readline()
    if not line:
        break
    if startNote == 1:
        deal_with_note(line)
    else:
        # if i > 1000:
        #    break
        i += 1

        m = re.search("<FormattedID>(.*)</FormattedID>", line)
        if m is not None:
            print "\n[[ " + m.group(1) + " ]]\n\n"
        else:
            m = re.search("<Notes>(.*)$", line)
            if m is not None:
                startNote = 1

myFile.close()




