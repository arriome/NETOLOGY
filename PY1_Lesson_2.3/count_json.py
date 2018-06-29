import re
import string
import collections
import sys
from collections import Counter
def count(file):
    frequency = {}
    
    #sys.setdefaultencoding('utf-8')
    #with open(file, "r", encoding="utf-8") as f:
    with open(file, "r") as f:
        text_string = f.read().lower()
        match_pattern = re.findall(r'\b[a-z]{6,}\b', text_string)
    c = collections.Counter(match_pattern)
    print("File name:",file)
    print(c.most_common(10))
count("newsfr.json")
count("newsit.json")
count("newsafr.json")
count("newscy.json.")
