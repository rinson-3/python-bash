#!/bin/bash

for fruit in peach orange apple; do
    echo "I like $fruit!"
done


# renaming the file with .HTM extension to .html example

#!/bin/bash
for file in .*HTM; do
    name=$(basename "$file" .HTM)
    mv "$file" "$name.html"
done