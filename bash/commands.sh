ls, chmod, cat, echo , cd mkdir, cp, touch 

# iostreams
# redirect the output of a command to a file instead of seeing in the screen

# use > to redirect the output
 eg- stdout.py > new_file.txt
# use >> to redirect the output and append the file
 eg- stdout.py >> new_file.txt

 # use < to redirect the input 
 eg- stdout.py < new_file.txt

  # use 2< to redirect the stderr
 eg- stdout.py < new_file.txt 2> error_file.txt

 # 2 represents the file descriptor of stderr stream
 # 0 and 1 represents the file descriptor of stdin and stdout stream

 # Piping - connects the output of 1 program to input of another
ls -l | less
cat haiku.txt | ./capitalize.py

# commands

ps- list all current running processes
free - amount of free memory
uptime - how long the computer has been on 