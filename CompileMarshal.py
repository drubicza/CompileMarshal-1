import os
import sys
import time
import marshal

sleep = time.sleep
GL    = '\x1b[96;1m'
WW    = '\x1b[0;1m'
CC    = '\x1b[36;1m'
MM    = '\x1b[1;41;36m'

os.system('clear')

print MM + 'Simple Marshal Compiler, By : B1G5M0K3 \x1b[0;0m'
print GL + '---------------------------------------'
print '\x1b[36;1m[#] \x1b[33;1mPath : \x1b[0;1m/path/nama.py'
print ''

kntl = raw_input('\x1b[0;1mMasukan File Anda : \x1b[30;0m')
sleep(2)
file = open(kntl).read()
com  = compile(file, '', 'exec')
dum  = marshal.dumps(com)

with open('jadi.py', 'w') as file_kntl:
    file_kntl.write('#Coded By : B1G5M0K3\n#GitHub : https://github.com/B1G5M0K3\nimport marshal\nexec(marshal.loads(' + repr(dum) + '))')

print '\x1b[32;1m[!] File Succes Compile : jadi.py\n'
print WW + '\n' + (type(dum), len(dum)) + '\n' + ('-' * 50) + '\n' + repr(dum) + '\n' + ('-' * 50)
