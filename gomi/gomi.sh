#!/bin/bash

wc popular-names.txt

sed -i '' 's/\t/ /g' popular-names.txt

cut -d ' ' -f 1 popular-names.txt>col.txt
cut -d ' ' -f 2 popular-names.txt>col2.txt

paste -d '\t' col.txt col2.txt > col3.txt

read num
head $((-num)) popular-names.txt

read num
tail -n $((-num)) popular-names.txt

read num
split -l $((num)) popular-names.txt

sort -f col.txt>file1.txt
uniq file1.txt>file2.txt

sort -k 3 -t ' ' -r popular-names.txt

sort -f col.txt | sort | uniq | sort -nr > file4.txt