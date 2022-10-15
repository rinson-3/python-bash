# variables
# globs - *?

#!/bin/bash
line="---------------------------------------"
echo "Starting at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)"


# conditions

#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then
    echo "Everything ok"
else
    echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi

# syntaxes

if test -n "$PATH"; then echo "Your path is not empty"; fi

if [ -n "$PATH" ]; then echo "Your path is not empty"; fi