import subprocess
import sys
import os.path

if __name__ == "__main__":
    argv = sys.argv[1:]
    if not argv:
        exit(0)
    if argv[0] !='python':
        argv.insert(0,'python')
    command = argv
    path = os.path.abspath('.')
    process = subprocess.Popen(command,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout_value,stderr_value = process.communicate()
    print(stdout_value,stderr_value)
