'''
tests for coreutils
'''

import os
import sys

ori_path_64 = "~/spec_2006/spec_2006_64_bit/{0}"
# res_path_64 = "~/spec_2006/spec_2006_64_bit_reproduce/"
ori_path_32 = "~/spec_2006/spec_2006_32_bit/{0}"
# res_path_32 = "~/spec_2006/spec_2006_32_bit_reproduce/"

exe_folder = {
    'perlbench_base': '400.perlbench',
    'bzip2_base': '401.bzip2',
    'gobmk_base': '445.gobmk',
    'hmmer_base': '456.hmmer',
    'libquantum_base': '462.libquantum',
    'milc_base': '433.milc',
    'sjeng_base': '458.sjeng',
    'gcc_base': '403.gcc',
    'h264ref_base': '464.h264ref',
    'lbm_base': '470.lbm',
    'mcf_base': '429.mcf',
    'sphinx_livepretend_base': '482.sphinx3'
}

all_benchmark = ''

for benchmark in exe_folder:
    all_benchmark += exe_folder[benchmark][4:] + ' '

exe_path = '~/spec_2006/SPEC_CPU2006v1.0/benchspec/CPU2006/{0}/exe/{1}'

a3_set = {'h264ref_base.i386-m32-gcc42-nn', 'gcc_base.i386-m32-gcc42-nn', 'gobmk_base.i386-m32-gcc42-nn',
          'perlbench_base.amd64-m64-gcc42-nn', 'gobmk_base.amd64-m64-gcc42-nn', 'gcc_base.amd64-m64-gcc42-nn'}
a2_set = {'gobmk_base.i386-m32-gcc42-nn',
          'gobmk_base.amd64-m64-gcc42-nn', 'gcc_base.amd64-m64-gcc42-nn'}

run_uroboros = "python ./../src/uroboros.py -o {0} {1} {2}"
# run_spec = 'runspec --config={0} --size=test,train,ref --noreportable --tune=base --iterations=1 {1}'
run_spec = 'runspec --config={0} --size=test --iterations=1 {1}'

config_x64 = 'test_64.cfg'
config_x86 = 'test_32.cfg'

os.system('cd ~/spec_2006/SPEC_CPU2006v1.0 && source ./shrc && cd $OLDPWD')

# x64 Loop
with open("spec_list_64") as f:
    lines = f.readlines()

for l in lines:
    file_name = l.strip()
    option = ""
    if file_name in a3_set:
        option += " -a 3"
    if file_name in a2_set:
        option += " -a 2"

    print '--------------', file_name, '------------------------'
    sys.stdout.flush()
    print run_uroboros.format(exe_path.format(
        exe_folder[file_name[:-19]], file_name), ori_path_64.format(file_name), option)
    os.system(run_uroboros.format(exe_path.format(
        exe_folder[file_name[:-19]], file_name), ori_path_64.format(file_name), option))
    print '-----------------------------------------------------'
    sys.stdout.flush()

raw_input(run_spec.format(config_x64, all_benchmark))
os.system(run_spec.format(config_x64, all_benchmark))

raw_input()

# x86 Loop
with open("spec_list_32") as f:
    lines=f.readlines()

for l in lines:
    file_name=l.strip()
    option=""
    if file_name in a3_set:
        option += " -a 3"
    if file_name in a2_set:
        option += " -a 2"

    print '--------------', file_name, '------------------------'
    sys.stdout.flush()
    print run_uroboros.format(exe_path.format(
        exe_folder[file_name[:-19]], file_name), ori_path_32.format(file_name), option)
    os.system(run_uroboros.format(exe_path.format(
        exe_folder[file_name[:-19]], file_name), ori_path_32.format(file_name), option))
    print '-----------------------------------------------------'
    sys.stdout.flush()

raw_input(run_spec.format(config_x86, all_benchmark))
os.system(run_spec.format(config_x86, all_benchmark))

