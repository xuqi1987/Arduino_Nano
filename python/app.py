#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'mayi'

import csv
import sys, getopt


def AnalysisCsv(name):
    with open(name,"r") as f:
        reader = csv.DictReader(f)
        Time = [ [int(row[' CS'].strip()), int(float(row['Time[s]'])*1000*1000)] for row in reader]

        strData = "uint32_t rawData[" + str(len(Time)) + "] = {"

        buffer = []
        for i in xrange(1,len(Time) -1):
            buffer.append(str(Time[i+1][1] - Time[i][1]))

        strData += ",".join(buffer)

        strData += "};"

        print strData
            #print str(Time[i][0])+ "\t" + str(Time[i+1][1] - Time[i][1]) + "\t" +str((Time[i+1][1] - Time[i][1])/16383)

if __name__ == "__main__":
    AnalysisCsv(sys.argv[1])