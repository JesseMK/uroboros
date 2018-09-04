'''
tests for coreutils
'''

import os
import sys

with open("core_list") as f:
    lines = f.readlines()

os.system("mv ~/coreutils/coreutils-8.15-32/src/test ~/coreutils/coreutils-8.15-32/src/test_bin")

for l in lines:
    print '--------------', l.strip(), '------------------------'
    sys.stdout.flush()
    os.system("python ./../src/uroboros.py ~/coreutils/coreutils-8.15-32/src/" + l.strip())
    os.system("mv ./../src/workdir/a.out ~/coreutils/coreutils-8.15-32/src_new/" + l.strip())
    print '-----------------------------------------------------'
    sys.stdout.flush()

os.system("rm ~/coreutils/coreutils-8.15-32/src_new/stdbuf")
os.system("mv ~/coreutils/coreutils-8.15-32/src_new/test_bin ~/coreutils/coreutils-8.15-32/src_new/test")
os.system("cp ~/coreutils/coreutils-8.15-32/src_new/*  ~/coreutils/coreutils-8.15-32/src/")
os.system("cd ~/coreutils/coreutils-8.15-32/ && make check")
