# unit tests - written to test the individual pieces like functions or methods
# tests should never modify our prod env    
import re

def rearrange_name(name):
    result=re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        return name
    return f"{result[2]} {result[1]}"