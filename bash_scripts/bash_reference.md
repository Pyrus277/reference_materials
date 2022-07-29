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
Get input and do some cumbersome arithmetic:
```bash
read -p 'Enter int value: ' x
read -p 'Enter int value: ' y

echo $((x+y))
echo $((x-y))
echo $((x*y))
echo $((x/y))
```


