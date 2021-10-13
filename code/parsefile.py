import csv
import os 
from sammaParser import logger

target = os.getenv('TARGET', 'samma.io')

with open("/output/{0}./{0}..txt".format(target)) as tsv:
    out=['','','','','','','','','','','','','','','','','','','','','','','','','','','','']
    for line in csv.reader(tsv, dialect="excel-tab"): 
        length = len(line)
        end= length -1
        for i in range(length):
            if line[i]:
                out[i] = line[i]
        out_line=""
        out_json={}
        for i in range(length):
            split = out[i].split(":")
            if len(split) >=2 :
                print(split)
                out_json[split[0]]=split[1]
            else:
                out_line=out_line+out[i].replace("-","")
            if i == end:
                #print("The last one")
                #out_json[out_line]= out[i]
                out_json[out[1]]=out_line.split()
        #print(out_json)
        logger(out_json)