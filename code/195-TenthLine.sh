# Read from the file file.txt and output the tenth line to stdout.
filename='file.txt'
n=1
while read line; do
if [ $n -eq 10 ]
then
echo $line
fi;
n=$((n+1))
done < $filename