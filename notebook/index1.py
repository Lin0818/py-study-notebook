#defaultdict: another take on missing keys
#collections.defaultdict 
'''
if 'new-key' is not in dd(defaultdict) then the expression dd['new-key'] does the following steps:
1. calls list() to create a new list
2. inserts the list into dd using 'new-key' as key
3. returns s reference to that list
'''
import sys
import re
import collections

WORD_RE = re.compile('\w+')

index = collections.defaultdict(list)
with open('test', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])
