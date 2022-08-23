# Read from the file words.txt and output the word frequency list to stdout.
awk '{ for (i=1;i<=NF;i++) { counts[$i]++ } } END { for (k in counts) { print(k, counts[k]) } }' words.txt | sort -nrk2