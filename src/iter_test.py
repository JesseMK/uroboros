'''
tests for coreutils
'''

import os
import sys

with open("core_list") as f:
    lines = f.readlines()

for l in lines:
    print '--------------', l.strip(), '------------------------'
    sys.stdout.flush()
    os.system("python uroboros.py /home/uroboros/coreutils-8.15-32/src/" + l.strip())
    os.system("mv workdir/a.out /home/uroboros/coreutils-8.15-32/src_new/" + l.strip())
    print '-----------------------------------------------------'
    sys.stdout.flush()
