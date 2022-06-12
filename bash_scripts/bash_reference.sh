# For any bash script your write, don't forget the first line: #!/bin/bash
# Also don't forget to make the file executable with chmod +x

###################################

# Use loops to display odd natural numbers from 1 to 99:

for i in {1..99..2}
do
    echo $i 
done

###################################

# loop thru a defined array (list)

# set your array
declare -a array=("apple" "pear" "cherry")
# now loop thru it
for i in "${array[@]}"
do
    echo "This $i is delicious!"
done

###################################
# Calling an index in an array!
$ declare -a array=("apple" "pear" "cherry")
$ echo ${array[1]} 

###################################

# Get a user input

read name
echo "Welcome, $name"

###################################

# While loops

echo "How many loops do you want?"
read LOOPS 

COUNT=1
while [ $COUNT -le $LOOPS ]
# can also use <= but need double parentheses
# while (( $COUNT <= $LOOPS ))
do
    echo "Loop# $COUNT "
    ((COUNT++)) # eq to ((COUNT = COUNT + 1))
done

# Note: [ -eq -ne -gt -ge -lt -le ] 
# ((< <= > >=))
#https://kapeli.com/cheat_sheets/Bash_Test_Operators.docset/Contents/Resources/Documents/index
###################################


# Get input and do some arithmetic

read -p 'Enter int value: ' x 
read -p 'Enter int value: ' y 

echo $((x+y))
echo $((x-y))
echo $((x*y))
echo $((x/y))

####################################

# Work some comparison operators in an IF statement

read x 
read y 

if (( $x < $y )); then echo "X is less than Y"
elif (( $x > $y )); then echo "X is greater than Y"
else echo "X is equal to Y"
fi

######################################

# if elif else control flow

echo "What food do you choose? "
read FOOD

if [ "$FOOD" = "Apple" ]; then
    echo "Eat yogurt with your apple."
elif [ "$FOOD" = "Milk" ]; then
    echo "Eat cereal with your milk."
else 
    echo "Eat your ${FOOD} by itself!"
fi


#####################################

# String comparisons with an or || statement-- seems to need an interior bracket set

read char

if [[ $char == y || $char == Y ]]; then echo "YES"
elif [[ $char == n || $char == N ]]; then echo "NO"
fi

#####################################

# Iterate a specified number of time and write output
# to a file that many times. 

echo "How many lines do you want?"
read LNS 

COUNT=1
while [ $COUNT -le $LNS ]
do
    echo "$COUNT $RANDOM" >> file.txt
    #echo "$COUNT $RANDOM $LNS" | tee -a file.txt 
    ((COUNT++))
done

# A useful tool: 
# $ shuf -n 5 file.txt 

######################################

# Find patterns:
$ grep apple filter-file.txt
# Count occurrences:
$ grep -c apple filter-file.txt
# Find either pattern
$ grep -e apple -e pear filter-file.txt
# Count occurrnces of both patterns
$ grep -c -e apple -e pear filter-file.txt
# Show all lines that DO NOT contain pattern
$ grep -v apple filter-file.txt

#########################################

# Searching for files

# Find all bash scripts
$ find . -name "*.sh"
# Find all CSV files
$ find . -name "*.csv"
# Find all executble non-invisible files
$ find . -perm /+x ! -name '.*' -type f
    # -perm /+x <---find everything with an execution flag on it
    # ! -name '.*' <---exclude file names that start with .
    # -type f <--- only include files (not dirs)

# find all executable non-invisible files and ignore .git dirs
$ find . -perm /+x -not -path '*/\.*' -type f
    # -not -path '*/\.*' -type f <--- ignore files in the path

####################################

# string slicing
$ echo "STRING" | cut -cN-M 
# Where N is index, and M is lenth.
# Use "cut -cN -" to get the single char.