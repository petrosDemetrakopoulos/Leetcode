# Read from the file file.txt and output all valid phone numbers to stdout.
regex1='^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
regex2='^[(][0-9]{3}[)][[:space:]][0-9]{3}[-][0-9]{4}$'

while read line; 
do if [[ "$line" =~ $regex1 ]]
then
   echo $line;
fi
if [[ "$line" =~ $regex2 ]]
then
   echo $line;
fi

done < file.txt