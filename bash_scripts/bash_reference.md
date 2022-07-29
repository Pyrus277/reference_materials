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
  
#### And now, a variety of patterns and syntaxes:

**Loops**  
This will display odd natural numbers from 1 to 99:
```bash
for i in {1..99..2} # {min(inclusive)..max(inclusive)..increment}
do
    echo $i
done
```
Output:
> 1  
> 3  
> 5  
> 7...  
  
Loop thru a defined array:
```bash
# Set the array
declare -a array=("apple" "pear" "cherry") 
# Iterate through it:
for i in "${array[@]}"
do
    echo "This $i is delicious!"
done
```
Output:
> This apple is delicious!
> This pear is delicious!
> This cherry is delicious!
