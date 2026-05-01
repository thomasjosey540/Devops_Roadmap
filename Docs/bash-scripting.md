# Bash Scripting Basics

## Echo

Print output to terminal.

echo "Hello DevOps"

---

## Variables

name="devops"
echo $name

---

## Command Line Arguments

echo $1
echo $2

---

## System Variables

echo $HOME
echo $USER

---

## Quotes

Single quotes:
echo 'Hello $name'  → no variable expansion

Double quotes:
echo "Hello $name"  → variable expands

---

## Command Substitution

current_date=$(date)
echo $current_date

---

## Export Variables

export VAR_NAME="value"

---

## User Input

read name
echo "Hello $name"

---

## If Statement

if [ $1 -eq 10 ]
then
  echo "Value is 10"
fi

---

## Loops

### For Loop
for i in 1 2 3
do
  echo $i
done

### While Loop
count=1
while [ $count -le 3 ]
do
  echo $count
  ((count++))
done

---

## Cron Jobs

Used to schedule tasks.

crontab -e

Example:
* * * * * /path/to/script.sh

---

## Remote Command Execution

ssh user@host "command"

---

## Real-World Use

- Automating tasks  
- Scheduling jobs  
- Managing systems remotely  

---

## Key Learning

- Bash scripting helps automate repetitive tasks  
- Essential for DevOps workflows  