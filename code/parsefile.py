import csv
import os 
from sammaParser import logger

target = os.getenv('TARGET', 'samma.io')

with open("/output/{0}./{0}..txt".format(target)) as tsv:
    out=['','','','','','','']
    for line in csv.reader(tsv, dialect="excel-tab"): 
        length = len(line)
        end= length -1
        for i in range(length):
            if line[i]:
                out[i] = line[i]
        out_line=""
        out_json={}
        for i in range(length):
            if i == end:
                print("The last one")
                out_json[out_line]= out[i]

            out_line=out_line+str(out[i]).replace(" ","-").replace(".","_")

        logger(out_json)