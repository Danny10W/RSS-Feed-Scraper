#!/bin/bash
python2 usererror.py > UserErrorQuestions.txt
python2 thenewshow.py > NewShowQuestions.txt
cat UserErrorQuestions.txt NewShowQuestions.txt > Combined.txt
sed -i 's/^ *//g' Combined.txt
sed -i 's/\#AskError\: //g' Combined.txt
sed -i 's/\#Askerror\: //g' Combined.txt
sed -i 's/#AskError //g' Combined.txt
sed -i 's/AskError: //g' Combined.txt
sort Combined.txt | uniq > NoRepeats.txt
sed '1d' NoRepeats.txt > FinalList.txt
rm NoRepeats.txt Combined.txt NewShowQuestions.txt UserErrorQuestions.txt