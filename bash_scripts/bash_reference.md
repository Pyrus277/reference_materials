## Bash Scripting

#### Any bash script opens with 
```bash
#!/bin/bash  
```
And of course, don't forget to change the permissions to executable. 
Also the file is run by sourcing it, with 'source' + script_name, or just '.' + script_name 
```bash
$ chmod +x <script_name>
$ . <script_name>
```
   
Running a bash script will start a child shell and any variables set in that script will only exist in the child shell.
To bring the contents of a script to the current shell you gotta run it with the source command as mentioned above.  
   
#### Annoying things to remember:
Spacing matters-   
No spaces before or after the = for assignments.  
Spaces within square brackets: [ content ]  
Letter comparison operators go with [ ] and symbolic ones go with (()):
[ -eq -ne -gt -lt -le ]  
((< <= > >=))   
https://kapeli.com/cheat_sheets/Bash_Test_Operators.docset/Contents/Resources/Documents/index



#### And now, a variety of patterns and syntaxes:

**Loops**  
This will display odd natural numbers from 1 to 99:
```bash
for i in {1..99..2} # {min(inclusive)..max(inclusive)..increment}
do
    echo $i
done
```
> 1  
> 3  
> 5  
> 7...  
  

**Loop** thru a defined **array**:
```bash
# Set the array
declare -a array=("apple" "pear" "cherry") 
# Iterate through it:
for i in "${array[@]}"
do
    echo "This $i is delicious!"
done
```
> This apple is delicious!  
> This pear is delicious!  
> This cherry is delicious!  
  
Calling an **index** in an **array**:
```bash
declare -a array=("apple" "pear" "cherry")
echo ${array[1]}
```
> pear

Get **user input**
```bash
read name
echo "Welcome, $name"
```
**While loop**
```bash
echo "How many loops do you want?"
read LOOPS

COUNT=1
while [ $COUNT -le $LOOPS ]
# Alternatively- (($COUNT <= $LOOPS))
do
    echo "Loop# $COUNT"
    ((COUNT++)) # bash syntax for COUNT += 1
done

```
Get input and do some cumbersome **arithmetic**:
```bash
read -p 'Enter int value: ' x
read -p 'Enter int value: ' y

echo $((x+y))
echo $((x-y))
echo $((x*y))
echo $((x/y))
```
**if elif else control flow**
```bash
echo "What food do you choose?"
read FOOD

if [ "$FOOD" = "Apple" ]; then
    echo "Eat yogurt with you apple."
elif [ "$FOOD" = "Milk" ]; then
    echo "Eat cereal with your milk."
else
    echo "Eat you ${FOOD} by itself!"
fi
```
**if statement + comparison operators**
```bash
if (($x < $y)); then echo "X is less than Y"
elif (( $x > $y )); then echo "X is greater than Y"
else echo "X is equal to Y"
fi
```
String comparisons with a || (or) statement.
This horrific syntax needs a set of interior brackets. 
```bash
echo "enter Y/N"
read char

if [[ $char == y || $char == Y ]]; then echo "YES"
elif [[ $char == n || $char == N ]]; then echo "NO"
fi
```
Iterate a specified number of times and write output to a file that many times.
```echo
echo "How many lines do you want?"
read LNS

COUNT=1
while [ $COUNT -le $LNS ]
do
    echo "$COUNT $RANDOM" >> file.txt
    # alternatively- this line writes to the file and gives a similar terminal output.
    # echo "$COUNT $RANDOM $LNS" | tee -a file.txt
    ((COUNT++))
done
```
**string slicing**
```bash
echo "STRING" | cut -cN-M
# Where N is the index, and M is length
# Use "cut -cN -" to get the single char. 


#### **grep**
Find patterns  
$ grep apple file.txt  
  
Count occurrences:  
$ grep -c apple file.txt  
  
Find either pattern  
$ grep -e apple -e pear file.txt  
  
Count occurrences of both patterns  
$ grep -c -e apple -e pear file.txt  
   
Show all lines that DO NOT contain pattern  
$ grep -v apple filter-file.txt  
  
#### Searching for files-- find
Find all bash scripts  
$ find . -name ".sh"  
  
Find all CSV files  
$ find . -name "\*.csv"  
  
Find all executable non-hidden files  
```bash
find . -perm /+x ! -name '.*' -type f
#    -perm /+x <--- find everything with en execution flag on it 
#    ! -name '.*' <--- exclude file names that start with .
#    -type f <---- only include files (not dirs)
```

Find all executable non-invisible files and ignore .git dirs
```bash
find . -perm /+x -not -path '*/\.*' -type f
```

