import re

file = open("../Day-3/Day-3.txt","r")
content = file.read()
p1 = r'mul\(\d{1,3},\d{1,3}\)'
p2 = action_pattern = r'(?:don\'t|do)\(\)'
p3 = f'({p1}|{p2})'
matches = re.findall(p3, content)

total = 0
bool = 0
p4 = r'mul\((\d+),(\d+)'

for pair in matches:
    if (pair == "don't()"):
        bool = 1
        continue
    if (pair == "do()"):
        bool = 0
        continue
    if bool == 0:
        match = re.search(p4, pair)
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        total += num1 * num2
    else: 
        continue

print(total)