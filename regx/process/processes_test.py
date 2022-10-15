import subprocess

# Subprocess - execute the system commands from python (ls,rm,sleep, etc) and check if they succeded or failed
# capture stdout and stderr and use their outputs in scripts



#print(subprocess.run(["date"]))

#print(subprocess.run(["sleep", "2"]))

#result=subprocess.run(["ls", "this_file_does_not_exist"])
#print(result.returncode)

result=subprocess.run(["host", "8.8.8.8"], capture_output=True)
#print(result.returncode)
#print(result.stdout)
#print(result.stdout.decode().split())

result=subprocess.run(["rm", "does_not_exist"], capture_output=True)
#print(result.returncode)
print(result.stdout)
print(result.stderr)



#  prepare a new environment (by adding a directory) to modify environment variables use copy()


import os
import subprocess

my_env=os.environ.copy()
my_env["PATH"]= os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result=subprocess.run(["myapp"], env=my_env)