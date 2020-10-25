todaysDate=$(date +"%A-%m-%d-%Y")
currentTime=$(date +"%I:%M %p")

base="$HOME/Projects/Journal/"
final="${base}${todaysDate}"

cd $base
git pull origin master

echo "" >> $final
echo "====================" >> $final
echo "===== "$currentTime" =====" >> $final
echo "====================" >> $final
echo "" >> $final
vim -c "startinsert" + $final

git add -A
git commit -m "no"
git push origin master
