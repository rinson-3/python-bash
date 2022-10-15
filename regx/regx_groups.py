# regx groups

import re

result=re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])

def rearrange_name(name):
    result=re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return print(f"{result[2]} {result[1]}")

rearrange_name("Davis, Rinson")
rearrange_name("Davis, Rinson I.")


def rearrange_name(name):
    result=re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result is None:
        return name
    return print(f"{result[2]} {result[1]}")

rearrange_name("Davis, Rinson")
rearrange_name("Davis, Rinson I.")
rearrange_name("Davis, Rinson I-")


print(re.search(r"[a-zA-Z]{5}", "a ghost"))
print(re.search(r"[a-zA-Z]{5}", "a ghost in a valley"))
print(re.findall(r"[a-zA-Z]{5}", "a ghost in a valley water"))
print(re.findall(r"\b[a-zA-Z]{5}\b", "a ghost in a valley water"))  # \b to indicate that we want words with 5 letters, its the word boundaries
print(re.findall(r"\w{5,10}", "a ghost in a valley water")) # prints words with 5 -10 letters

print(re.findall(r"\w{5,}", "a ghost in a valley water errsrtres5rtffxvcncvnxv"))

print(re.search(r"e\w{,50}", "a ghost in a valley water errsrtres5rtffxvcncvnxv"))

log="July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex=r"\[(\d+)\]"
result=re.search(regex, log)
print(result[1])

log="July 31 07:51:48 mycomputer bad_process: ERROR Performing package upgrade[3495]"
regex=r"\[(\d+)\]"
result=re.search(regex, log)
print(result[1])

log="July 31 07:51:48 mycomputer bad_process: ERROR Performing package upgrade[test]"

# log="July 31 07:51:48 mycomputer bad_process: ERROR Performing package upgrade[test]"
# regex=r"\[(\d+)\]"
# result=re.search(regex, log)
# print(result[1])
  
# pid is the process id   
def extract_pid(log_line):
    regex=r"\[(\d+)\]"
    result=re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]

print(extract_pid(log))


import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]\[A-Z]" # need to update here
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)



# split 

test=re.split(r"[.?!]", "One sentence. Anoter one? and last one!")
print(test)

test=re.split(r"([.?!])", "One sentence. Anoter one? and last one!") 
print(test)

test=re.split(r"the|a", "One sentence. Another one? And the last one!")
print(test)

test=re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")
print(test)

test=re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
print(test)