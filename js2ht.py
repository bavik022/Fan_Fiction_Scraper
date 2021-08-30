import json
from json2html import *
import os

for filename in os.listdir("E:\Assignments\Text Technology Project"):
    if filename.endswith(".json"):
        fin = open(filename, "r")
        inp = json.load(fin)
        fin.close()
        html = json2html.convert(json = inp, table_attributes="id=\"info-table\" class=\"table table-bordered table-hover\"")
        outfile = filename.split(".")
        f = open(outfile[0]+".html", "w")
        f.write(html)  
        f.close()