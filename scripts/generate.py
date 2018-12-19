import json
import sys
import subprocess

syscalls = set()
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        syscalls.add(line.strip())

foo = {
    "defaultAction": "SCMP_ACT_ERRNO",
    "architectures": [
       "SCMP_ARCH_X86_64",
       "SCMP_ARCH_X86",
       "SCMP_ARCH_X32"
    ],
    "syscalls": []
}

for i in syscalls:
    item = {
        "name": i,
        "action": "SCMP_ACT_ALLOW",
        "args": []
    }

    foo['syscalls'].append(item)
    with open(sys.argv[2], 'w') as f:
        f.write(json.dumps(foo, indent=2))
