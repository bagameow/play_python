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


def deal_with_name(line):
    m = re.search("<Name>(.*)</Name>", line)
    if m:
        print "\n[Name] " + m.group(1)
        return True
    return False

def deal_with_id(line):
    m = re.search("<FormattedID>(.*)</FormattedID>", line)
    if m:
        print "\n=============================================================\n\n[ID] " + m.group(1)
        return True
    return False

myFile = open("parsed.xml", "r")
startNote = 0


def found_begin_of_note(line):
    global startNote
    m = re.search("<Notes>(.*)$", line)
    if m:
        print "\n[Note]\n\n" + m.group(1)
        startNote = 1
        return True
    return False

i = 0


def deal_with_test_folder(line):
    m = re.search("<TestFolder ", line)
    if m:
        m2 = re.search("refObjectName=\"(.*)\" type=", line)
        if m2:
            print "\n[TestFolder] " + m2.group(1) + "\n"
            return True
        else:
            exit(-1)
    return False

while True:
    i += 1
    line = myFile.readline()
    if not line:
        break

    if startNote == 1:
        deal_with_note(line)
    elif deal_with_id(line):
        pass
    elif deal_with_name(line):
        pass
    elif found_begin_of_note(line):
        pass
    elif deal_with_test_folder(line):
        pass

    if i > 1000:
        break

myFile.close()




