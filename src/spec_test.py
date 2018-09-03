'''
tests for coreutils
'''

import os
import sys

ori_path_64 = "~/spec_2006/spec_2006_64_bit/"
res_path_64 = "~/spec_2006/spec_2006_64_bit_reproduce/"
ori_path_32 = "~/spec_2006/spec_2006_32_bit/"
res_path_32 = "~/spec_2006/spec_2006_32_bit_reproduce/"

a3_set = {'h264ref_base.i386-m32-gcc42-nn', 'gcc_base.i386-m32-gcc42-nn', 'gobmk_base.i386-m32-gcc42-nn',
          'perlbench_base.amd64-m64-gcc42-nn', 'gobmk_base.amd64-m64-gcc42-nn', 'gcc_base.amd64-m64-gcc42-nn'}
a2_set = {'gobmk_base.i386-m32-gcc42-nn',
          'gobmk_base.amd64-m64-gcc42-nn', 'gcc_base.amd64-m64-gcc42-nn'}

with open("spec_list_64") as f:
    lines = f.readlines()

for l in lines:
    file_name = l.strip()
    option = ""
    if file_name in a3_set:
        option += " -a 3 "
    if file_name in a2_set:
        option += " -a 2 "

    print '--------------', file_name, '------------------------'
    sys.stdout.flush()
    command = "python uroboros.py -o " + res_path_64 + \
        file_name + " " + ori_path_64 + file_name + option
    os.system(command)
    print '-----------------------------------------------------'
    sys.stdout.flush()

with open("spec_list_32") as f:
    lines = f.readlines()

for l in lines:
    file_name = l.strip()
    option = ""
    if file_name in a3_set:
        option += " -a 3 "
    if file_name in a2_set:
        option += " -a 2 "

    print '--------------', file_name, '------------------------'
    sys.stdout.flush()
    command = "python uroboros.py -o " + res_path_32 + \
        file_name + " " + ori_path_32 + file_name + option
    os.system(command)
    print '-----------------------------------------------------'
    sys.stdout.flush()