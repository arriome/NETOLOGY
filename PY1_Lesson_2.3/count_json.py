import re
import string
#import sys
import chardet  
from collections import Counter
def count(file):
    #frequency = {}    
    #sys.setdefaultencoding('utf-8')
    #with open(file, "r", encoding="utf-8") as f:  
    with open(file, "rb") as f:        
        text_string = f.read()
        result = chardet.detect(text_string)        
        text_enc = result['encoding']        
    with open(file, "r", text_enc) as f2:     
        text_string2 = f2.read().lower()
        match_pattern = re.findall(r'\b[a-z]{6,}\b', text_string2)
    c = collections.Counter(match_pattern)
    print("File name:",file)
    print(c.most_common(10))
count("newsfr.json")
count("newsit.json")
count("newsafr.json")
count("newscy.json.")
