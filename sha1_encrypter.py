#!/usr/bin/python3

from hashlib import sha1
import sys



#sha1 encrypt
def make_sha1(line, encoding='utf-8'):
    return sha1(line.encode(encoding)).hexdigest()

filepath = sys.argv[1]
newfile = sys.argv[2]
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        #print Initial value:
        #print(line.strip())

        #print hashed sha1 value:
        #print(make_sha1(line.strip(), encoding='utf-8'))

        #write to file:
        with open(newfile, 'a') as nf:
            nf.write(make_sha1(line.strip(), encoding='utf-8'))
            nf.write("\n")
        line = fp.readline()
        cnt += 1
        
print("Wordlist Created: "+str(sys.argv[2]))
